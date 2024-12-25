import ttkbootstrap as ttk
from prayer_times import read_prayer_times
from dynamic_updater import DynamicUpdater
from PIL import Image, ImageTk

# GREEN = "#3E7D5D"
GREEN = "#127958"
DARKER_GREEN = "#0E6146"
LIGHTER_GREEN = "#16916A"
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
    self.prayer_times_component = PrayerTimesComponenet(self, self.updater)

class PrayerTimesComponenet(ttk.Frame):
  def __init__(self, parent, updater):
    super().__init__(parent)
    self.updater = updater 
    self.pack(fill='both', expand=True)
    self.prayer_times_widgets()
  
  def prayer_times_widgets(self):
    
    main_frame = ttk.Frame(self)
    main_background = ttk.Label(main_frame, background=GREEN)

    # Clock Label
    clock = ttk.Label(main_frame, background=DARKER_GREEN, font=('Montserrat', 55, 'bold'), foreground=GOLD, anchor='center')

    # Date Label

    date = ttk.Label(main_frame, font=('Helvetica', 25, 'bold', 'italic'), foreground=GOLD, background = DARKER_GREEN, anchor='center')

    # Prayer Times Frame

    prayer_info = ttk.Label(main_frame, text=f'{"ATHAAN    IQAMAH":>45}', background=GREEN, font=('Helvetica', 25, 'bold'), foreground=GOLD, anchor='s')


    prayer_label_font = ('Consolas', 40, 'bold')
    prayer_label_foreground = GOLD

    fajr_label = ttk.Label(main_frame, text='Fajr', font = prayer_label_font, foreground=prayer_label_foreground, background=GREEN, anchor='center')

    sunrise_label = ttk.Label(main_frame, text='Sunrise', font= prayer_label_font, foreground=prayer_label_foreground, background=GREEN, anchor='center')

    dhuhr_label = ttk.Label(main_frame, text='Dhuhr', font= prayer_label_font, foreground=prayer_label_foreground, background=GREEN, anchor='center')

    asr_label = ttk.Label(main_frame, text='Asr', font= prayer_label_font, foreground=prayer_label_foreground, background=DGRAY, anchor='center')

    maghrib_label = ttk.Label(main_frame, text='Maghrib', font= prayer_label_font, foreground=prayer_label_foreground, background=GREEN, anchor='center')
    
    isha_label = ttk.Label(main_frame, text='Isha', font= prayer_label_font, foreground=prayer_label_foreground,background=GREEN, anchor='center')

    def pack_widgets():
      main_frame.pack(side='left', fill='both', expand=True)
      main_background.pack(fill='both', expand=True)

      clock.place(relx=0, rely=0, relheight=0.20, relwidth=1)
      date.place(relx=0, rely=0.17, relheight=0.08, relwidth=1)  

      prayer_info.place(relx=0, rely=0.25, relheight=0.05, relwidth=1)  

      label_height = 0.70 / 6
      fajr_label.place(relx=0.01, rely=0.30, relheight=label_height, relwidth=1)
      sunrise_label.place(relx=0.01, rely=0.30 + label_height, relheight=label_height, relwidth=0.98)
      dhuhr_label.place(relx=0.01, rely=0.30 + 2 * label_height, relheight=label_height, relwidth=0.98)
      asr_label.place(relx=0.01, rely=0.30 + 3 * label_height, relheight=label_height, relwidth=0.98)
      maghrib_label.place(relx=0.01, rely=0.30 + 4 * label_height, relheight=label_height, relwidth=0.98)
      isha_label.place(relx=0.01, rely=0.30 + 5 * label_height, relheight=label_height, relwidth=0.98)
    
    def dynamic_update():
      self.updater.update_clock(clock)
      self.updater.update_date(date, None)
      self.updater.update_prayer_times({'Fajr':fajr_label, 'Sunrise':sunrise_label, 'Dhuhr':dhuhr_label, "Asr":asr_label, 'Maghrib':maghrib_label, 'Isha':isha_label})


    pack_widgets()
    dynamic_update()
      


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





