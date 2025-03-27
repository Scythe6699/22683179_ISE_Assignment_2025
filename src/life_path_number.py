def life_path_number(day, month, year):
    # master numbers
    master_num = [11, 22, 33]

    # add digits
    def add_digit(data):
        total = 0
        for digit in str(data):
            total += int(digit)
        
        return total
    
    # greater than 9
    def greater_formatter(num):
        if num <= 9:
            return num
        return greater_formatter(add_digit(num))

    # life path check

    ## check if any of them are masters
    if day not in master_num:
        day = greater_formatter(day)

    if month not in master_num:
        month = greater_formatter(month)

    if year not in master_num:
        year = greater_formatter(year)

    ## total
    total = day + month + year

    ## check if total is master
    _is_master_ = False
    if total in master_num:
        _is_master_ = True
        return total, _is_master_

    ## sum of total digits
    output = add_digit(total)
    
    return output, _is_master_
