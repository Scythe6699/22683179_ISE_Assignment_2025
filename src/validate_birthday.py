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

    # check year
    if 0 > year > 2025:
        raise ValueError("Invalid year!\nError: Out of range")


    

