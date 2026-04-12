def clock_convert(time, ampm):
    # time = 1:23
    # ampm = pm
    hr,min = time.split(":")
    hr = int(hr)
    min = int(min)

    total_min = int(hr)*60 + int(min)

    # thf -> 24 hr format time. e.g. 13:04
    # If the time is AM and the hour is 12, convert hour to 00.
    if ampm == "am" and hr == "12":
        thf = f"00:{min}:"
    
    # If the time is between 1:00 AM and 12:59 PM, 24 hour time is same as 12 hour time.
    if 60<= total_min <= 779:
        thf = time
    
    # If the time is between 1:00 PM and 11:59 PM, we add 12 hours to input time.
    if 60<= total_min <= 719 and ampm == "pm":
        thf = f"{hr+12}:{min}"
    
    return thf

