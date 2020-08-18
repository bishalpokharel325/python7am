#datetime module vanne filne nabanaunu...
#import garne and date time garne


#today kotime k cha vanne
import datetime
print(datetime.date.today())

#time
dm=datetime.date.today()
#Monday 0 and Sunday 0
print(dm.weekday())
#monday 1 sunday 7
print(dm.isoweekday())
 
#different time ko formate dekhaune
dftm=datetime.timedelta(days=7)
print(dm-dftm)

#date set ni garna sakchau
#job expire vako time patta launu paryo deadline cha vanera aucha ni testo format pattalaune wa afnai birthday kaile chavanera findout garnu paryo
bdy=datetime.date(2020,11,21)
timefrombdday=bdy-dm
print(timefrombdday.days)
#variable lai store garera check ni garna sakchau
#sapai hamle system ko tiem garim
#format lai change garnu paro vane?
print(dm.strftime("%d--%B--%Y"))
print(datetime.time)
#class matra ayo
#time matra chaiyo vane
import time
import calendar
print(dir(time))
#exact time date nai chaio
print(datetime.datetime.now())
#calender ni import garna sakincha. .calkender nai print huncha
# print(calendar.calendar(2020))
#timzone ko lagi alagai huncha pytz vanne
#cmd kholer pip list garyo vane list aucha..
#pip install pytz garne for time zone
import pytz
for tz in pytz.all_timezones:
     print(tz)







