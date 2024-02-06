from datetime import datetime, timedelta

current_date = datetime.now()

# Finding the current month's first Tuesday
first_day_of_month = current_date.replace(day=1)
first_tuesday = first_day_of_month + timedelta(days=(1 - first_day_of_month.weekday()) % 7) 

print(first_day_of_month)
print(first_tuesday)

