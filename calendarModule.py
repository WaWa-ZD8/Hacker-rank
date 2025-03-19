import calendar
month_date_year = list(map(int,(input().split())))

which_day = calendar.weekday(month_date_year[2], month_date_year[0], month_date_year[1])
print(calendar.day_name[which_day].upper())

