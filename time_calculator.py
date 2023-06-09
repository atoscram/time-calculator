
def add_time(start_time, duration, start_day=None):
    # example
    # add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM
    end_day = ""
    days_of_the_week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    time, meridien = start_time.split()
    time_hours, time_minutes = time.split(":")
    duration_hours, duration_minutes = duration.split(":")

    # Convert 12 hour format time to 24 hour format
    if meridien.lower() == "pm":
        time_hours = int(time_hours) + 12

    added_minutes = int(time_minutes) + int(duration_minutes)
    added_hours = int(time_hours) + int(duration_hours) + int(added_minutes // 60)

    # Floating days value with decimal hours
    passed_days = added_hours / 24
    # Floating hour value with decimal minutes
    passed_hours = added_minutes / 60
    # Current hour in 24 hr format
    current_hour = added_hours % 24
    # Current minutes
    current_minute = added_minutes % 60

    # Convert to 12-hour format
    if current_hour == 0:
        current_hour_12_format = 12
        meridien = "AM"
    elif current_hour == 12:
        current_hour_12_format = current_hour
        meridien = "PM"
    elif current_hour > 11:
        current_hour_12_format = current_hour - 12
        meridien = "PM"
    else:
        current_hour_12_format = current_hour
        meridien = "AM"

    # Calculate the end_day if start day is provided
    if start_day:
        day_index = 0

        for day in days_of_the_week:
            if day.lower() == start_day.lower():
                break
            else:
                day_index += 1

        if day_index > 7:
            print('Error: start day is not right')

        total_days = day_index + int(passed_days // 1)

        end_day = ", " + days_of_the_week[total_days % 7]

    if int(passed_days) == 0:
        # same day
        return str(current_hour_12_format) + ":" + str(int(current_minute)).zfill(2) + " " + meridien + end_day
    elif int(passed_days) == 1:
        # next day
        return str(current_hour_12_format) + ":" + str(int(current_minute)).zfill(2) + " " + meridien + end_day + " (next day)"
    else:
        # days have passed
        return str(current_hour_12_format) + ":" + str(int(current_minute)).zfill(2) + " " + meridien + end_day + " (" + str(int(passed_days)) + " days later)"



