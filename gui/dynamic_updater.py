import time
from datetime import datetime, timedelta
from hijri_converter import convert

class DynamicUpdater:
    def __init__(self, root, prayer_times):
        self.root = root
        self.prayer_times = prayer_times
        self.iqamah_config = {
            'Fajr': {'fixed': '7:00 AM'},
            'Sunrise': None,
            'Dhuhr': {'fixed': '1:00 PM'},
            'Asr': {'offset_minutes': 5},
            'Maghrib': {'offset_minutes': 5},
            'Isha': {'offset_minutes': 10},
        }
        self.today_iqamah_times = {'Fajr': None, 'Dhuhr': None, 'Asr': None, 'Maghrib': None, 'Isha': None}
        self.compute_iqamah_times()
        self.check_iqamah_times()

    def update_clock(self, live_clock):
        current_time = time.strftime("%I:%M %p")
        if current_time[0] == '0':
            current_time = current_time[1:]

        live_clock.config(text=current_time)
        live_clock.after(1000, lambda: self.update_clock(live_clock))

    def update_date(self, live_date, live_hijri_date):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        current_date_str_len = len(current_date)

        #hijri_date_obj = convert.Gregorian(datetime.now().year, datetime.now().month, datetime.now().day).to_hijri()
        #hijri_date_str = f"{hijri_date_obj.day} {hijri_date_obj.month_name()} {hijri_date_obj.year} AH"

        live_date.config(text=f'{current_date:>{current_date_str_len}}')
        #live_hijri_date.config(text=f'{hijri_date_str:<{current_date_str_len}}')
        live_date.after(1000, lambda: self.update_date(live_date, live_hijri_date))

    def compute_iqamah_times(self):
        current_month = datetime.now().strftime('%B')
        current_day = int(datetime.now().strftime('%d'))

        today_prayer_times = self.prayer_times[current_month][current_day]
        iqamah_times = {}

        for prayer_name, iqamah_info in self.iqamah_config.items():
            if iqamah_info is None:
                continue
            if 'fixed' in iqamah_info:
                iqamah_time_str = iqamah_info['fixed']
                iqamah_time = datetime.strptime(str(iqamah_time_str), '%I:%M %p')
                iqamah_time = iqamah_time.replace(year=datetime.now().year,
                                                  month=datetime.now().month,
                                                  day=datetime.now().day)
            elif 'offset_minutes' in iqamah_info:
                # Get the prayer time
                prayer_time_str = today_prayer_times[prayer_name]
                prayer_time = datetime.strptime(prayer_time_str, '%I:%M %p')
                prayer_time = prayer_time.replace(year=datetime.now().year,
                                                  month=datetime.now().month,
                                                  day=datetime.now().day)
                iqamah_time = prayer_time + timedelta(minutes=iqamah_info['offset_minutes'])
            else:
                continue
            iqamah_times[prayer_name] = iqamah_time

        self.today_iqamah_times = iqamah_times

        # Schedule to recompute after midnight
        now = datetime.now()
        midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        seconds_until_midnight = (midnight - now).total_seconds()
        self.root.after(int(seconds_until_midnight * 1000), self.compute_iqamah_times)

    def update_prayer_times(self, prayer_time_entries):
        current_month = datetime.now().strftime('%B')
        current_day = int(datetime.now().strftime('%d'))

        today_prayer_times = self.prayer_times[current_month][current_day]

        prayer_time_entries['fajr']['adhan'].config(text = f" {today_prayer_times['Fajr'].replace('AM', '').replace('PM', '').strip()}")
        prayer_time_entries['fajr']['iqamah'].config(text = f"{'7:00'}")

        prayer_time_entries['sunrise']['adhan'].config(text = f" {today_prayer_times['Sunrise'].replace('AM', '').replace('PM', '').strip()}")
        
        prayer_time_entries['dhuhr']['adhan'].config(text = f"{today_prayer_times['Dhuhr'].replace('AM', '').replace('PM', '').strip()}")
        prayer_time_entries['dhuhr']['iqamah'].config(text = f"{'1:00'}")

        prayer_time_entries['asr']['adhan'].config(text = f" {today_prayer_times['Asr'].replace('AM', '').replace('PM', '').strip()}")
        prayer_time_entries['asr']['iqamah'].config(text = f"{self.today_iqamah_times['Asr'].strftime('%I:%M').lstrip('0')}")

        prayer_time_entries['maghrib']['adhan'].config(text = f" {today_prayer_times['Maghrib'].replace('AM', '').replace('PM', '').strip()}")
        prayer_time_entries['maghrib']['iqamah'].config(text = f"{self.today_iqamah_times['Maghrib'].strftime('%I:%M').lstrip('0')}")

        prayer_time_entries['isha']['adhan'].config(text = f" {today_prayer_times['Isha'].replace('AM', '').replace('PM', '').strip()}")
        prayer_time_entries['isha']['iqamah'].config(text = f"{self.today_iqamah_times['Isha'].strftime('%I:%M').lstrip('0')}")

        # Schedule next update
        (prayer_time_entries['fajr']['adhan']).after(1000, lambda: self.update_prayer_times(prayer_time_entries))

    def countdown(self, countdown_prayer_label, countdown_time_label):
        next_prayer, time_difference = self.next_prayer_time()
        time_difference -= 0

        hours, remainder = divmod(time_difference, 3600)
        minutes, seconds = divmod(remainder, 60)

        countdown_str_prayer = f"{next_prayer:2} {'is':2} {'in':2} : "
        countdown_str_time = f"{int(hours):02} : {int(minutes):02} : {int(seconds):02}"

        countdown_prayer_label.config(text=countdown_str_prayer.upper())
        countdown_time_label.config(text=countdown_str_time)

        countdown_time_label.after(1000, lambda: self.countdown(countdown_prayer_label, countdown_time_label))

    def next_prayer_time(self):
        current_time = datetime.now()
        current_month = current_time.strftime('%B')
        current_day = int(current_time.strftime('%d'))

        today_prayer_times = self.prayer_times[current_month][current_day]

        time_format = "%I:%M %p"

        for prayer, prayer_time_str in today_prayer_times.items():
            prayer_time = datetime.strptime(prayer_time_str, time_format)
            prayer_time = prayer_time.replace(year=current_time.year, month=current_time.month, day=current_time.day)

            if prayer_time > current_time:
                time_difference = (prayer_time - current_time).total_seconds()
                return prayer, time_difference

        # If no more prayers today, get the first prayer of tomorrow
        tomorrow = current_time + timedelta(days=1)
        tomorrow_month = tomorrow.strftime('%B')
        tomorrow_day = int(tomorrow.strftime('%d'))
        tomorrow_prayer_times = self.prayer_times[tomorrow_month][tomorrow_day]

        for prayer, prayer_time_str in tomorrow_prayer_times.items():
            prayer_time = datetime.strptime(prayer_time_str, time_format)
            prayer_time = prayer_time.replace(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day)

            time_difference = (prayer_time - current_time).total_seconds()
            return prayer, time_difference

    def check_iqamah_times(self):
        current_time = datetime.now()
        for prayer_name, iqamah_time in self.today_iqamah_times.items():
            if iqamah_time <= current_time < iqamah_time + timedelta(seconds=1):
                # Iqamah time just hit
                # self.show_duaa_screen()
                break

        # Schedule the next check
        self.root.after(1000, self.check_iqamah_times)

