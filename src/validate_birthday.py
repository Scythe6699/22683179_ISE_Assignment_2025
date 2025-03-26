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
    
    # check day, month & year range
    if (0 > year > 2025) or (0 > int(month) > 12) or (0 > int(day) > 31):
        raise ValueError("Invalid Input!\nError: Out of range")
    
    _is_leap_ = False
    # check if leap year
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
        _is_leap_ = True
    
    # calendar
    calendar = {
        1: ["january", 31],
        2: ["february", 28],
        3: ["march", 31],
        4: ["april", 30],
        5: ["may", 31],
        6: ["june", 30],
        7: ["july", 31],
        8: ["august", 31],
        9: ["september", 31],
        10: ["october", 31],
        11: ["november", 31],
        12: ["december", 31]
    }

    

    
