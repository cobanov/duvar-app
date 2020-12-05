import datetime

time = datetime.datetime.today() + datetime.timedelta(hours=3)
print(time.strftime("%m.%d.%Y, %H:%M") )