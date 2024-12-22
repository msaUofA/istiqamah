import ttkbootstrap as ttk
from prayer_times import read_prayer_times
from dynamic_updater import DynamicUpdater
from PIL import Image, ImageTk

# GREEN = "#3E7D5D"
GREEN = "#127958"
GOLD  = "#D4AF37"
WHITE = "#F5F5F5"
DGRAY = "#141414"
LGRAY = "#A9A9A9"


class GUI(ttk.Toplevel):
  def __init__(self):
    super().__init__()
    self.attributes('-fullscreen', True)
    self.bind('<Escape>', lambda event: self.quit())
    self.configure(background='black')
    self.prayer_times = read_prayer_times('prayertimes.csv')
    self.updater = DynamicUpdater(self, self.prayer_times)
    self.main_frame = MainFrame(self, self.updater)
  
  def run(self):
    self.mainloop()

class MainFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.pack(fill='both', expand=True)

    # Frames
    LeftFrame(self, self.updater).place(relx=0, rely=0, relheight=1, relwidth=0.43)
    RightFrame(self, self.updater).place(relx=0.43, rely=0, relheight=1, relwidth=0.60)


class LeftFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.label = ttk.Label(self, text='Left Frame', font=('Helvetica', 24), background=GREEN).pack(fill='both', expand=True) 

class RightFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.label = ttk.Label(self, text='Right Frame', font=('Helvetica', 24), background=WHITE).pack(fill='both', expand=True) 