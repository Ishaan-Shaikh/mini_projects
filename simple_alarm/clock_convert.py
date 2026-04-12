def clock_convert(time, ampm):
    hr, min = time.split(":")
    hr = int(hr)
    min = int(min)
    total_min = hr * 60 + min

    # 12:xx AM -> 00:xx
    if ampm == "am" and hr == 12:
        thf = f"00:{min:02d}"

    # 1:00 AM - 11:59 AM: no change needed
    elif ampm == "am" and 1 <= hr <= 11:
        thf = time

    # 12:xx PM -> 12:xx (no change needed)
    elif ampm == "pm" and hr == 12:
        thf = time

    # 1:00 PM - 11:59 PM: add 12 hours
    elif ampm == "pm" and 1 <= hr <= 11:
        thf = f"{hr + 12}:{min:02d}"

    return thf