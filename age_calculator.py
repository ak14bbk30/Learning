import datetime as dt
import time

date= str(input("enter date of birth in %d/%m/%Y"))
while(True):
    time.sleep(1)

    current_time=dt.datetime.now()


    dob=dt.datetime.strptime(date,'%d/%m/%Y')

    actual_age_in_year=current_time-dob

    years = ((actual_age_in_year.total_seconds())/(365.2421196*24*3600))
    yearsInt=int(years)



    months=(years-yearsInt)*12
    monthsInt=int(months)

    days=(months-monthsInt)*(365.2421196/12)
    daysInt=int(days)

    hours = (days-daysInt)*24
    hoursInt=int(hours)
    minutes = (hours-hoursInt)*60
    minutesInt=int(minutes)

    seconds = (minutes-minutesInt)*60
    secondsInt =int(seconds)

    print(yearsInt,"years",monthsInt,"months",daysInt,"days (",hoursInt,":",minutesInt,":",secondsInt,')')






