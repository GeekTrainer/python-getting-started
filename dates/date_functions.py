#To get current date and time we need to use the datetime library
import datetime
# The now function returns current date and time
today = datetime.datetime.now()

print('Today is: ' + str(today))
#You can use timedelta to add or remove days, or weeks to a date
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = datetime.timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

