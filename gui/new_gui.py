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

background_style = ttk.Style()
background_style.configure('Frame', background=DGRAY)


class GUI(ttk.Toplevel):
  def __init__(self):
    super().__init__()
    self.attributes('-fullscreen', True)
    self.bind('<Escape>', lambda event: self.quit())
    self.configure(background='black')
    self.prayer_times = read_prayer_times('prayertimes.csv')
    self.updater = DynamicUpdater(self, self.prayer_times)
    
    # Frames
    LeftFrame(self, self.updater)
    RightFrame(self, self.updater)
  
  def run(self):
    self.mainloop()


class LeftFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.place(relx=0, rely=0, relheight=1, relwidth=0.43)
    self.label = ttk.Label(self, text='Left Frame', font=('Helvetica', 24), background=DGRAY).pack(fill='both', expand=True) 

class RightFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.place(relx=0.43, rely=0, relheight=1, relwidth=0.60)
    self.logo = ImageTk.PhotoImage((Image.open('Assets/msalogo.png').resize((240, 120))))
    self.widgets()
  
  def widgets(self):

    main_frame = ttk.Frame(self)
    main_background = ttk.Label(main_frame, background=GREEN)

    # Countdown Frame
    countdown_frame = ttk.Frame(main_frame)
    countdown_prayer = ttk.Label(countdown_frame, font=("Helvetica", 70, 'bold'), foreground=GOLD, background=GREEN, anchor='center')
    countdown_time = ttk.Label(countdown_frame, font=("Helvetica", 65, 'bold'), foreground=GOLD, background=GREEN, anchor='center')

    countdown_headers_frame = ttk.Frame(main_frame)
    countdown_headers_frame.background = ttk.Label(countdown_headers_frame, background=GOLD)
    hour_header = ttk.Label(countdown_headers_frame, text='Hours', font=('Helvetica', 20, 'bold'), foreground=GREEN, background=WHITE)
    minute_header = ttk.Label(countdown_headers_frame, text='Minutes', font=('Helvetica', 20, 'bold'), foreground=GREEN, background=WHITE)
    second_header = ttk.Label(countdown_headers_frame, text='Seconds', font=('Helvetica', 20, 'bold'), foreground=GREEN, background=WHITE)

    def pack_widgets():
      main_frame.pack(fill='both', expand=True)
      main_background.pack(fill='both', expand=True)
      countdown_frame.place(relx=0, rely=0.34, relheight=0.24, relwidth=1)
      countdown_prayer.pack(side='top', fill='x') 
      countdown_time.pack(fill='x') 
      countdown_headers_frame.place(relx=0, rely=0.58, relheight=0.1, relwidth=1)
      countdown_headers_frame.background.pack(fill='both', expand=True)

    
    def dynamic_update():
      self.updater.countdown(countdown_prayer, countdown_time)
    
    pack_widgets()
    dynamic_update()







