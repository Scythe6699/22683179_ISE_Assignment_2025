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
        elif num in master_num:
            return num
        return greater_formatter(add_digit(num))
    
    # life path check
    ## get the individual sums
    day_sum = day if day in master_num else greater_formatter(day)
    month_sum = month if month in master_num else greater_formatter(month)
    year_sum = year if year in master_num else greater_formatter(year)
    
    ## total
    total = day_sum + month_sum + year_sum
    
    ## check if total is a master number or needs further reduction
    if total in master_num:
        return total
    elif total > 9:
        return greater_formatter(total)
    
    return total