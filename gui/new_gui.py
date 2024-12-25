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
    self.label = ttk.Label(self, text='Left Frame', font=('Helvetica', 24), background=GREEN).pack(fill='both', expand=True)


class RightFrame(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater
    self.place(relx=0.43, rely=0, relheight=1, relwidth=0.60)
    self.logo = ImageTk.PhotoImage((Image.open('Assets/msalogo.png').resize((240, 120))))
    self.countdown_component = CountdownComponent(self, self.updater)
    self.event_component = None
    self.create_widgets()

  def create_widgets(self):

    logo_frame = ttk.Frame(self)
    logo_label = ttk.Label(logo_frame, image=self.logo, background=DGRAY, anchor='center') 

    def pack_widgets():
      
      logo_frame.place(relx=0, rely=0, relheight=0.25, relwidth=1)
      logo_label.pack(fill='both', expand=True)
    
    pack_widgets()


class CountdownComponent(ttk.Frame):

  def __init__(self, parent, updater):
    super().__init__(parent)
    self.pack(fill='both', expand=True)
    self.updater = updater
    self.countdown_widgets()
      
  def countdown_widgets(self):


    main_frame = ttk.Frame(self)
    main_background = ttk.Label(main_frame, background=DGRAY)

    # Countdown Frame
    countdown_frame = ttk.Frame(main_frame)
    countdown_prayer = ttk.Label(countdown_frame, font=("Helvetica", 70, 'bold'), foreground=GOLD, background=DGRAY, anchor='center')
    countdown_time = ttk.Label(countdown_frame, font=("Helvetica", 65, 'bold'), foreground=GOLD, background=DGRAY, anchor='center')

    # Countdown Headers Frame
    countdown_headers_frame = ttk.Frame(main_frame)
    countdown_headers_frame.background = ttk.Label(countdown_headers_frame, background=DGRAY)
    hour_header = ttk.Label(countdown_headers_frame, text='HOURS', font=('Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')
    minute_header = ttk.Label(countdown_headers_frame, text='MINUTES', font=('Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')
    second_header = ttk.Label(countdown_headers_frame, text='SECONDS', font=('Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')

    def pack_widgets():
      main_frame.pack(side = 'left', fill='both', expand=True)
      main_background.pack(fill='both', expand=True)
      countdown_frame.place(relx=0, rely=0.34, relheight=0.24, relwidth=1)
      countdown_prayer.pack(side='top', fill='x') 
      countdown_time.pack(fill='x') 
      countdown_headers_frame.place(relx=0, rely=0.60, relheight=0.2, relwidth=1)
      countdown_headers_frame.background.pack(fill='both', expand=True)
      hour_header.place(relx= 0.239, rely=0, relheight=0.28, relwidth=0.13)
      minute_header.place(relx=0.439, rely=0, relheight=0.28, relwidth=0.13)
      second_header.place(relx=0.639, rely=0, relheight=0.28, relwidth=0.13)
    
    def dynamic_update():
      self.updater.countdown(countdown_prayer, countdown_time)
    
    pack_widgets()
    dynamic_update()

class EventComponent(ttk.Frame):
  pass





