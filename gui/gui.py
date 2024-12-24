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



class PrayerTimeGUI(ttk.Toplevel):
    def __init__(self):
        # Main window
        super().__init__()
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda event: self.quit())

        # Read prayer times
        self.prayer_times = read_prayer_times('prayertimes.csv')

        # Initialize DynamicUpdater
        self.updater = DynamicUpdater(self, self.prayer_times)

        # Frames
        self.main_top_frame = TopFrame(self, self.updater)
        self.main_bottom_frame = BottomFrame(self, self.updater)

    def run(self):
        self.mainloop()
        
class TopFrame(ttk.Frame):
    def __init__(self, parent, updater):
        super().__init__(parent)
        self.updater = updater
        self.place(x=0, y=0, relheight=0.7, relwidth=1)
        logo = Image.open('../Assets/msalogo.png')
        logo = logo.resize((240, 120))
        self.logo = ImageTk.PhotoImage(logo)
        self.create_widget()
        s = ttk.Style()
        s.configure('TFrame', background=DGRAY)
        s.configure('TLabel', background=DGRAY)

    def create_widget(self):
        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background=GREEN)

        data_frame = ttk.Frame(main_frame)
        title_frame = ttk.Frame(data_frame)
        clock_frame = ttk.Frame(data_frame)

        logo = Image.open('../Assets/msalogo.png')
        logo = logo.resize((240,120))  
        self.logo = ImageTk.PhotoImage(logo)  

        title_label = ttk.Label(title_frame, image=self.logo, background=DGRAY, anchor='center')

        date = ttk.Label(title_frame, font=('Helvetica', 20, 'bold', 'italic'), foreground=GREEN, anchor='n')
        hijri_date = ttk.Label(title_frame, font=('Helvetica', 20, 'bold', 'italic'), foreground=GREEN, anchor='n')

        live_clock = ttk.Label(clock_frame, font=('Times New Roman', 40, 'bold'), foreground=GOLD, anchor='n')
        countdown = ttk.Label(clock_frame, font=("Times New Roman", 100, 'bold'), foreground=GOLD, anchor='n')

        def pack_widgets():
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            date.pack(side='left', expand=True, fill='x')
            title_label.pack(side='left', expand=True, fill='x', padx=150)
            hijri_date.pack(side='left', expand=True, fill='x')
            countdown.pack(expand=True, fill='both')
            live_clock.pack(expand=True, fill='both')
            title_frame.pack(expand=True, fill='x')
            clock_frame.pack(expand=True, fill='both')
            data_frame.pack(expand=True, fill='both', padx=10, pady=10)
            main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        pack_widgets()
        self.updater.update_clock(live_clock)
        self.updater.update_date(date, hijri_date)
        self.updater.countdown(countdown)



class BottomFrame(ttk.Frame):
    def __init__(self, parent, updater):
        super().__init__(parent)
        self.updater = updater
        self.place(x=0, rely=0.7, relheight=0.3, relwidth=1)
        self.create_widgets()
        s = ttk.Style()
        s.configure('TFrame', background=DGRAY)

    def create_widgets(self):
        def add_separator(parent):
            separator_frame = ttk.Frame(parent, width=2)
            separator_frame.pack(side='left', fill='y', pady=20) 

            separator = ttk.Separator(separator_frame, orient='vertical')
            separator.pack(expand=True, fill='y') 

        main_frame = ttk.Frame(self)
        background_label = ttk.Label(main_frame, background=GREEN)
        prayer_times_frame = ttk.Frame(main_frame)

        fajr = PrayerTimeEntry(prayer_times_frame, 'Fajr', "0")
        add_separator(prayer_times_frame)

        sunrise = PrayerTimeEntry(prayer_times_frame, 'Sunrise', "0")
        add_separator(prayer_times_frame)

        dhuhr = PrayerTimeEntry(prayer_times_frame, 'Dhuhr', "0")
        add_separator(prayer_times_frame)

        asr = PrayerTimeEntry(prayer_times_frame, 'Asr', "0")
        add_separator(prayer_times_frame)

        maghrib = PrayerTimeEntry(prayer_times_frame, 'Maghrib', "0")
        add_separator(prayer_times_frame)

        isha = PrayerTimeEntry(prayer_times_frame, 'Isha', "0")

        prayer_widgets = {
            'Fajr': fajr,
            'Sunrise': sunrise,
            'Dhuhr': dhuhr,
            'Asr': asr,
            'Maghrib': maghrib,
            'Isha': isha
        }

        def pack_widgets():
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            main_frame.pack(expand=True, fill='both', padx=10, pady=5)
            prayer_times_frame.pack(expand=True, fill='both', padx=10, pady=10)

        pack_widgets()
        self.updater.update_prayer_times(self, prayer_widgets)

class PrayerTimeEntry(ttk.Frame):
    def __init__(self, parent, prayer_name, prayer_time):
        super().__init__(parent, style='light')
        self.pack(side='left', expand=True, fill='both')

        text_color = GOLD

        self.prayer_name_label = ttk.Label(self, text=prayer_name, font=('Times New Roman', 40, 'bold'), anchor='center', foreground=text_color)
        self.prayer_name_label.pack(expand=True, fill='both')

        self.prayer_time_label = ttk.Label(self, text=prayer_time, font=('Times New Roman', 40), anchor='center', foreground=text_color)
        self.prayer_time_label.pack(expand=True, fill='both')

        if prayer_name == 'Fajr':
            ttk.Label(self, text="Iqamah: 7:00AM", font=('Times New Roman', 16, 'bold'), anchor='center',foreground=WHITE).pack(expand=True, fill='both')

        if prayer_name == 'Sunrise':
                ttk.Label(self).pack(expand=True, fill='both')

        if prayer_name == 'Dhuhr':
            ttk.Label(self, text="Iqamah: 1:00PM", font=('Times New Roman', 16, 'bold'), anchor='center', foreground=WHITE).pack(expand=True, fill='both')

        if prayer_name == 'Asr':
            ttk.Label(self, text="Iqamah: Asr + 5 minutes", font=('Times New Roman', 16, 'bold'), anchor='center', foreground=WHITE).pack(expand=True, fill='both')

        if prayer_name == 'Maghrib':
            ttk.Label(self, text="Iqamah: Maghrib + 5 minutes", font=('Times New Roman', 16, 'bold'), anchor='center', foreground=WHITE).pack(expand=True, fill='both')

        if prayer_name == 'Isha':
            ttk.Label(self, text="Iqamah: Isha + 10 minutes", font=('Times New Roman', 16, 'bold'), anchor='center', foreground=WHITE).pack(expand=True, fill='both')


    def update_time(self, new_prayer_time):
        self.prayer_time_label.config(text=new_prayer_time)


PrayerTimeGUI()

