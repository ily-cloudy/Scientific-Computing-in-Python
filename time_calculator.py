def add_time(start, duration, day=""):
    #parameters
    weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    if day != "":
        day = day.lower()
        if day in weekdays == False:
            return "Error: please use a valid day of the week."
    
    #parsing input
    if "PM" in start:
        start = start.replace(" PM","")
        time = 12 * 60
    elif "AM" in start:
        start = start.replace(" AM","")
        time = 0
    else:
        return "Error: please use a valid time."

    # time calculation
    start = start.split(":")
    time = time + int(start[0]) * 60 + int(start[1])
    duration = duration.split(":")
    time = time + int(duration[0]) * 60 + int(duration[1])

    # output value calculation
    days = int(time/1440)
    hours = int((time%1440)/60)
    minutes = int((time%1440)%60)
    
    # ffs americans dont understand numbers > 12

    if hours == 0:
      str_M = " AM"
      hours = 12
    elif hours > 12:
      str_M = " PM"
      hours = hours - 12
    elif hours == 12:
      str_M = " PM"
    elif hours < 12:
      str_M = " AM"

    #output formatting
    if days == 0:
        str_add = ""
    elif days == 1:
        str_add = " (next day)"
    elif days > 1:
        str_add = f" ({days} days later)"
  
    if day == "":
        str_d = ""
    else:
        day_index = weekdays.index(day) + days
        if day_index > 6:
            day_i = day_index%7
        try:
          day = weekdays[day_i]
        except:
          day = weekdays[day_index]
        day = day.title()
        str_d = f", {day}"
    
    str_h = str(hours)
    if minutes < 10:
        str_m = "0" + str(minutes)
    else:
        str_m = str(minutes)

    new_time = str_h + ":" + str_m + str_M + str_d + str_add

    return new_time