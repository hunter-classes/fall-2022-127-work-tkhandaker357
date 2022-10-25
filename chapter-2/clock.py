time_now = input("What hour is it now?: ")
alarm_wait = input("How long to wait for the alarm?: ")

total_time = int(time_now) + int(alarm_wait)

if total_time > 24:
  days_past = total_time / 24
  total_time = int(days_past + int(time_now))
  
print("Your alarm will go off at", total_time, "(24Hr Time)")