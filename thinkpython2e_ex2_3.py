import datetime

start_time = 6 * 60 **2 + 52 * 60
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12
total_time = start_time + easy_pace + tempo_pace *3 + easy_pace

print(datetime.timedelta(seconds=total_time))