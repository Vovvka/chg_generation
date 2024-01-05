from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Example usage:
start_description = '3rd week After Patch Tuesday'
start_time = '6PM, Sunday'
duration_hours = 6

def get_date_range(start_description, start_time, duration_hours):
    print("Received Input:")
    print(f"Start Description: {start_description}")
    print(f"Start Time: {start_time}")
    print(f"Duration (hours): {duration_hours}")

    if ',' in start_time:
        time_parts = start_time.split(', ')
        specified_time = time_parts[0]
        specified_day = time_parts[1]
    
    description_parts = start_description.split()
    
    start_time_24h = datetime.strptime(specified_time, "%I%p").strftime("%H:%M")

    current_date = datetime.now()

    # Finding the next Monday after the first Tuesday (Patch Tuesday)
    first_day_of_month = current_date.replace(day=1)
    first_tuesday = first_day_of_month + timedelta(days=(1 - first_day_of_month.weekday()) % 7)
    patch_tuesday = first_tuesday + timedelta(days=6)
    next_monday = patch_tuesday + timedelta(days=(7 - patch_tuesday.weekday()) % 7)
        
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_indices = {day: index for index, day in enumerate(day_names)}
    
    start_datetime = None
    end_datetime = None

    if 'next'.lower() in ' '.join(description_parts).lower():
        
        print("Executing 'Next Month' logic...")
        # Extracting the month
        current_date = current_date.replace(day=1) + relativedelta(months=1)
        
        # Extracting numeric value for weekday selection (1st, 2nd, 3rd, 4th)
        weekday_selection = int(start_description.split()[0][:-len("th")])
        
        # Calculating the selected weekday of the next month
        first_day_of_next_month = current_date.replace(day=1)
        selected_weekday = day_indices[specified_day.capitalize()]
        current_weekday = first_day_of_next_month.weekday()
        diff = (selected_weekday - current_weekday) % 7
        start_date = first_day_of_next_month + timedelta(days=diff + 7 * (weekday_selection - 1))

        # Constructing start date and time
        start_datetime = datetime.strptime(f"{start_date.date()} {start_time_24h}", "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(hours=duration_hours)

        print("\nFinal Calculated Dates:")
        print(f"Start Date: {start_datetime.strftime('%Y-%m-%d %H:%M')}")
        print(f"End Date: {end_datetime.strftime('%Y-%m-%d %H:%M')}")

        return start_datetime.strftime("%Y-%m-%d %H:%M"), end_datetime.strftime("%Y-%m-%d %H:%M")
        
    elif 'after'.lower() in ' '.join(description_parts).lower():

        print("Executing 'after Patch Tuesday' logic...")
        if description_parts[0] == '0':
            start_day_index = day_indices[specified_day.capitalize()] - next_monday.weekday()
        else:
            # Extracting the week offset
            week_offset = int(description_parts[0][:-2])
            # Calculate the starting day index within the desired week after Patch Tuesday
            start_day_index = (day_indices[specified_day.capitalize()] - next_monday.weekday() + 7) % 7
            # Adjust to the specified week within the month
            start_day_index += week_offset * 7
            # Adjust if the start_day_index is negative
            if start_day_index < 0:
                start_day_index += 7
        
        # Constructing start date and time
        start_date = next_monday + timedelta(days=start_day_index)
        start_datetime = datetime.strptime(f"{start_date.date()} {start_time_24h}", "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + timedelta(hours=duration_hours)

        print("\nFinal Calculated Dates:")
        print(f"Start Date: {start_datetime.strftime('%Y-%m-%d %H:%M')}")
        print(f"End Date: {end_datetime.strftime('%Y-%m-%d %H:%M')}")

        return start_datetime.strftime("%Y-%m-%d %H:%M"), end_datetime.strftime("%Y-%m-%d %H:%M")

    else:
        # Handle other cases or return an error message for unhandled cases
        return "Error: Invalid description", ""

start_date_formatted, end_date_formatted = get_date_range(start_description, start_time, duration_hours)
if start_date_formatted and end_date_formatted:
    print("\nFinal Output:")
    print(f"Start Date: {start_date_formatted}")
    print(f"End Date: {end_date_formatted}")
