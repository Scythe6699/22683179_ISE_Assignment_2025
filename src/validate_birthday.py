def validate_birthday(birthday):
    birthday_list = str(birthday).split()

    # handle error when input not in the correct format
    if len(birthday_list) < 3:
        raise ValueError("Invalid Input!\nError: Incorrect Format!")

    # get the data
    day = birthday_list[0]
    month = birthday_list[1]
    year = birthday_list[0]

    # check day and year
    if (day.isdigit() == False) or (year.isdigit() == False):
        raise ValueError("Invalid Input!\nError: Invalid Day or Year!")
    
    # check day & year range
    if (0 > year > 2025) or (0 > int(day) > 31):
        raise ValueError("Invalid Input!\nError: Out of range")
    
    _is_leap_ = False
    # check if leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        _is_leap_ = True
    
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

    # check month
    if (month.lower() not in calendar) and (month.lower() not in calendar_abbr):
        raise ValueError("Invalid Input!\nError: Invalid Month!")
    
    
