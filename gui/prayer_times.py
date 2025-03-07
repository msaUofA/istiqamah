import csv
import datetime
from datetime import datetime


def read_prayer_times(filename: str):

    prayer_times = {}
    current_month = None

    with open(filename, mode='r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:
            if any(month in row for month in ['January', 'February', 'March', 'April', 'May', 'June',
                                              'July', 'August', 'September', 'October', 'November', 'December']):
                current_month = row[1]
                if current_month not in prayer_times:
                    prayer_times[current_month] = {}

            elif row[0] and current_month:
                prayer_times[current_month][int(row[1])] = {
                    'Fajr': row[2],
                    'Sunrise': row[3],
                    'Dhuhr': row[4],
                    'Asr': row[5],
                    'Maghrib': row[6],
                    'Isha': row[7]
                }

    return prayer_times


def next_prayer_time(prayer_times: dict):

    current_month = datetime.now().strftime('%B')
    current_day = datetime.now().strftime('%d')
    current_time = datetime.now()

    today_prayer_times = prayer_times[current_month][int(current_day)]
    tomorrow_prayer_times = prayer_times[current_month][int(current_day) + 1]

    time_format = "%I:%M %p"

    for prayer, prayer_time in today_prayer_times.items():

        prayer_time = datetime.strptime(prayer_time, time_format)

        prayer_time = prayer_time.replace(
            year=current_time.year, month=current_time.month, day=current_time.day)

        if prayer_time > current_time:

            time_difference = (prayer_time - current_time).total_seconds()

            return prayer, time_difference

    for prayer, prayer_time_str in tomorrow_prayer_times.items():

        prayer_time = datetime.strptime(prayer_time_str, time_format)
        prayer_time = prayer_time.replace(
            year=current_time.year, month=current_time.month, day=int(current_day) + 1)

        time_difference = (prayer_time - current_time).total_seconds()

        return prayer, time_difference
