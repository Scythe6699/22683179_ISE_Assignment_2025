# import modules
import src.validate_birthday, src.life_path_number, src.lucky_color, src.generation_checker

# user input
birthday = input("Enter your birthday (e.g., 09 July 2005 or 13 Nov 1987): ")

# validate birthday
day, month, year = src.validate_birthday.validate_birthday(birthday=birthday)

# life path number
lpn = src.life_path_number.life_path_number(day=day, month=month, year=year)

# lucky color
lc = src.lucky_color.lucky_color(lpn=lpn)

# generation
gen = src.generation_checker.generation_checker(year=year)

# print output
print(f"\nYour brithday         : {birthday}")
print(f"Your life path number : {lpn}")
print(f"Your luck color       : {lc}")
print(f"Your generation       : {gen}")
