import datetime

print("How many seconds are there in 42 minutes, 42 seconds?")
print(42 * 60 + 42)

print("How many miles are there in 10 kilometers?")
print(10 / 1.61)

print("If you run a 10 kilometer race in 42 minutes, 42 seconds, what is your average pace?")
pace_in_sec = 2562 / 6.2
print(datetime.timedelta(seconds=pace_in_sec))

print("What is your average speed in miles per hour?")
minutes = 42 + 42/60
print(6.2/minutes)
