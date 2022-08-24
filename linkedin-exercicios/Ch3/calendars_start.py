#
# Example file for working with Calendars
#

# import the calendar module
import calendar
import datetime
from datetime import date
from datetime import datetime

now = datetime.now()
print(now.strftime("%d-%b-%Y %H:%M:%S"))
print("now.strftime :", now.strftime("%c"))

today = date.today()
print("Today = ", today)
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# print("Tomorrow will be "+days[today.weekday()+1])


# print("datetime.date   :", datetime.date(datetime.now()))

# create a plain text calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2022, 7, 0, 0)
# print(st)

# create a plain text calenar for the year of 2022
# print("Calendario de 2022")
# cal = calendar.TextCalendar(calendar.SUNDAY)
# for m in range(1, 12):
#     print(cal.formatmonth(2022, m, 0, 0))


# today = date.today()
# print("Today = ", today)
# print("Hoje :", today.day)

# create an HTML formatted calendar

# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2022,1)
# print (st)


# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2022,8):
#     print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

# print("Team meetings will be on: ")
# for m in range(1, 13):
#     cal = calendar.monthcalendar(2022, m)
#     weekone = cal[0]
#     weektwo = cal[1]

#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]

#     print("%10s %2d" % (calendar.month_name[m], meetday))
