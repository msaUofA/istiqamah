import ttkbootstrap as ttk
from prayer_times import read_prayer_times
from dynamic_updater import DynamicUpdater
from PIL import Image, ImageTk
from pathlib import Path

# GREEN = "#3E7D5D"
ROOT_DIR = Path(__file__).resolve().parent.parent
GREEN = "#127958"
DARKER_GREEN = "#0E6146"
LIGHTER_GREEN = "#16916A"
GOLD = "#D4AF37"
WHITE = "#F5F5F5"
DGRAY = "#141414"
LGRAY = "#A9A9A9"


class GUI(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda event: self.quit())
        self.configure(background='black')
        self.prayer_times = read_prayer_times(ROOT_DIR / 'prayertimes2025.csv')
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
        clock = ttk.Label(main_frame, background=DARKER_GREEN, font=(
            'Helvetica', 75, 'bold'), foreground=GOLD, anchor='center')

        # Date Label

        date = ttk.Label(main_frame, font=('Helvetica', 35, 'bold', 'italic'),
                         foreground=GOLD, background=DARKER_GREEN, anchor='center')

        # Prayer Times Frame

        prayer_times_frame = ttk.Frame(main_frame)
        prayer_times_frame.background = ttk.Label(
            prayer_times_frame, background=GREEN)

        prayer_info_frame = ttk.Label(prayer_times_frame, text=f'{"ATHAAN   IQAMAH":>48}', background=GREEN, font=(
            'Helvetica', 33, 'bold'), foreground=GOLD, anchor='s')

        prayer_label_master = prayer_times_frame
        prayer_label_anchor = 'center'
        prayer_label_font = ('Arial', 60, 'bold')
        prayer_label_foreground = GOLD

        def create_prayer_label(str):
            return ttk.Label(prayer_label_master, text=str, font=prayer_label_font, foreground=prayer_label_foreground, background=GREEN, anchor=prayer_label_anchor)

        fajr_label = create_prayer_label('Fajr')
        fajr_adhan_label = create_prayer_label('6:00 AM')
        fajr_iqamah_label = create_prayer_label('6:15 AM')

        sunrise_label = create_prayer_label('Sunrise')
        sunrise_adhan_label = create_prayer_label('6:00 AM')
        sunrise_iqamah_label = create_prayer_label("")

        dhuhr_label = create_prayer_label('Dhuhr')
        dhuhr_adhan_label = create_prayer_label('1:00 PM')
        dhuhr_iqamah_label = create_prayer_label('1:15 PM')

        asr_label = create_prayer_label('Asr')
        asr_adhan_label = create_prayer_label('3:00 PM')
        asr_iqamah_label = create_prayer_label('3:15 PM')

        maghrib_label = create_prayer_label('Maghrib')
        maghrib_adhan_label = create_prayer_label('6:00 PM')
        maghrib_iqamah_label = create_prayer_label('6:15 PM')

        isha_label = create_prayer_label('Isha')
        isha_adhan_label = create_prayer_label('8:00 PM')
        isha_iqamah_label = create_prayer_label('8:15 PM')

        def pack_widgets():
            main_frame.pack(side='left', fill='both', expand=True)
            main_background.pack(fill='both', expand=True)

            clock.place(relx=0, rely=0, relheight=0.15, relwidth=1)
            date.place(relx=0, rely=0.14, relheight=0.08, relwidth=1)

            # Prayer Times Frame
            prayer_times_frame.place(
                relx=0, rely=0.22, relheight=0.78, relwidth=1)
            prayer_times_frame.background.pack(fill='both', expand=True)

            prayer_info_frame.place(relx=0, rely=0, relheight=0.06, relwidth=1)

            fajr_label.place(relx=0.01, rely=0.07,
                             relheight=0.15, relwidth=0.45)
            fajr_adhan_label.place(relx=0.46, rely=0.07,
                                   relheight=0.15, relwidth=0.285)
            fajr_iqamah_label.place(
                relx=0.745, rely=0.07, relheight=0.15, relwidth=0.245)

            sunrise_label.place(relx=0.01, rely=0.22,
                                relheight=0.15, relwidth=0.45)
            sunrise_adhan_label.place(
                relx=0.46, rely=0.22, relheight=0.15, relwidth=0.285)
            sunrise_iqamah_label.place(
                relx=0.745, rely=0.22, relheight=0.15, relwidth=0.245)

            dhuhr_label.place(relx=0.01, rely=0.37,
                              relheight=0.15, relwidth=0.45)
            dhuhr_adhan_label.place(
                relx=0.46, rely=0.37, relheight=0.15, relwidth=0.285)
            dhuhr_iqamah_label.place(
                relx=0.745, rely=0.37, relheight=0.15, relwidth=0.245)

            asr_label.place(relx=0.01, rely=0.52,
                            relheight=0.15, relwidth=0.45)
            asr_adhan_label.place(relx=0.46, rely=0.52,
                                  relheight=0.15, relwidth=0.285)
            asr_iqamah_label.place(relx=0.745, rely=0.52,
                                   relheight=0.15, relwidth=0.245)

            maghrib_label.place(relx=0.01, rely=0.67,
                                relheight=0.15, relwidth=0.45)
            maghrib_adhan_label.place(
                relx=0.46, rely=0.67, relheight=0.15, relwidth=0.285)
            maghrib_iqamah_label.place(
                relx=0.745, rely=0.67, relheight=0.15, relwidth=0.245)

            isha_label.place(relx=0.01, rely=0.82,
                             relheight=0.15, relwidth=0.45)
            isha_adhan_label.place(relx=0.46, rely=0.82,
                                   relheight=0.15, relwidth=0.285)
            isha_iqamah_label.place(
                relx=0.745, rely=0.82, relheight=0.15, relwidth=0.245)

        def dynamic_update():
            self.updater.update_clock(clock)
            self.updater.update_date(date, None)
            self.updater.update_prayer_times({'fajr': {'adhan': fajr_adhan_label, 'iqamah': fajr_iqamah_label},
                                              'sunrise': {'adhan': sunrise_adhan_label},
                                              'dhuhr': {'adhan': dhuhr_adhan_label, 'iqamah': dhuhr_iqamah_label},
                                              'asr': {'adhan': asr_adhan_label, 'iqamah': asr_iqamah_label},
                                              'maghrib': {'adhan': maghrib_adhan_label, 'iqamah': maghrib_iqamah_label},
                                              'isha': {'adhan': isha_adhan_label, 'iqamah': isha_iqamah_label}})

        pack_widgets()
        dynamic_update()


class RightFrame(ttk.Frame):
    def __init__(self, parent, updater):
        super().__init__(parent)
        self.updater = updater
        self.place(relx=0.43, rely=0, relheight=1, relwidth=0.60)
        self.logo = ImageTk.PhotoImage(
            (Image.open(ROOT_DIR / 'Assets' / 'msalogo.png').resize((360, 180))))
        self.countdown_component = CountdownComponent(self, self.updater)
        self.event_component = None
        self.create_widgets()

    def create_widgets(self):

        logo_frame = ttk.Frame(self)
        logo_label = ttk.Label(logo_frame, image=self.logo,
                               background=DGRAY, anchor='center')

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
        countdown_prayer = ttk.Label(countdown_frame, font=(
            "Helvetica", 95, 'bold'), foreground=GOLD, background=DGRAY, anchor='center')
        countdown_time = ttk.Label(countdown_frame, font=(
            "Helvetica", 85, 'bold'), foreground=GOLD, background=DGRAY, anchor='center')

        # Countdown Headers Frame
        countdown_headers_frame = ttk.Frame(main_frame)
        countdown_headers_frame_background = ttk.Label(
            countdown_headers_frame, background=DGRAY)
        hour_header = ttk.Label(countdown_headers_frame, text='HOURS', font=(
            'Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')
        minute_header = ttk.Label(countdown_headers_frame, text='MINUTES', font=(
            'Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')
        second_header = ttk.Label(countdown_headers_frame, text='SECONDS', font=(
            'Arial', 15, 'bold', 'italic'), foreground=DGRAY, background=GOLD, anchor='center')

        def pack_widgets():
            main_frame.pack(side='left', fill='both', expand=True)
            main_background.pack(fill='both', expand=True)
            countdown_frame.place(
                relx=0, rely=0.34, relheight=0.24, relwidth=1)
            countdown_prayer.pack(side='top', fill='x')
            countdown_time.pack(fill='x')
            countdown_headers_frame.place(
                relx=0, rely=0.6, relheight=0.2, relwidth=1)
            countdown_headers_frame_background.pack(fill='both', expand=True)
            hour_header.place(relx=0.239, rely=0,
                              relheight=0.28, relwidth=0.13)
            minute_header.place(relx=0.439, rely=0,
                                relheight=0.28, relwidth=0.13)
            second_header.place(relx=0.639, rely=0,
                                relheight=0.28, relwidth=0.13)

        def dynamic_update():
            self.updater.countdown(countdown_prayer, countdown_time)

        pack_widgets()
        dynamic_update()
