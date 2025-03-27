def validate_birthday(birthday):
    # correct format
    birthday_list = str(birthday).split()
    if len(birthday_list) < 3:
        raise ValueError("Invalid Input!\nError: Incorrect Format!")
    
    # get the data
    day = birthday_list[0]
    month = birthday_list[1]
    year = birthday_list[2]
    
    # check day and year
    if (not day.isdigit()) or (not year.isdigit()):
        raise ValueError("Invalid Input!\nError: Invalid Day or Year!")
    
    # convert day and year to int
    day = int(day)
    year = int(year)
    
    # check day & year range
    if year < 0 or year > 2025 or day < 1 or day > 31:
        raise ValueError("Invalid Input!\nError: Out of range")
    
    # calendar
    calendar = {
        "january": [1, 31],
        "february": [2, 28],
        "march": [3, 31],
        "april": [4, 30],
        "may": [5, 31],
        "june": [6, 30],
        "july": [7, 31],
        "august": [8, 31],
        "september": [9, 30],
        "october": [10, 31],
        "november": [11, 30],
        "december": [12, 31]
    }
    
    # month name abbreviations --> e.g., "jan": "january"
    calendar_abbr = {m[:3]: m for m in calendar.keys()}
    
    # check if leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        calendar["february"] = [2, 29]
        calendar_abbr["feb"] = [2, 29]
    
    # normalize month
    month = month.lower()
    if month in calendar_abbr:
        month = calendar_abbr[month]
    
    # check month
    if month not in calendar:
        raise ValueError("Invalid Input!\nError: Invalid Month!")
    
    # check day
    max_day = calendar[month][1]
    if day > max_day:
        raise ValueError("Invalid Input!\nError: Invalid Day!")
    
    # return
    return day, calendar[month][0], year
