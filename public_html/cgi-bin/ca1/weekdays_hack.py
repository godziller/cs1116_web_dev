from datetime import date, datetime, timedelta

time = datetime.now()
print(time)
today = date.today()
print(today)
print(today.weekday())
print(timedelta(days=today.weekday()))

"""
This weeks slot
"""
start_of_week = today - timedelta(days=today.weekday())  # Monday of this week
end_of_week = start_of_week + timedelta(days=6)          # Sunday of this week

print('This week')
print(start_of_week)
print(end_of_week)

"""
Next Weeks Slot
Find out how many days to the start of next week by  7 - todays number, then add it to today.
"""
start_of_next_week = today + timedelta(days=(7 - today.weekday()))  # Monday of next week
end_of_next_week = start_of_next_week + timedelta(days=6)                 # Sunday of next week

print('Next Week')
print(start_of_next_week )
print(end_of_next_week)
"""
Note to self
Looks like Monday (weekday()) = 0, Tue  = 1, .... Sun = 6"""