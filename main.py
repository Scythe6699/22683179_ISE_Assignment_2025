# import modules
from src.validate_birthday import validate_birthday
from src.life_path_number import life_path_number
from src.lucky_color import lucky_color
from src.generation_checker import generation_checker

def main():
    # user input
    birthday = input("Enter your birthday (e.g., 09 July 2005 or 13 Nov 1987): ")
    
    # validate birthday
    day, month, year = validate_birthday(birthday=birthday)
    
    # life path number
    lpn = life_path_number(day=day, month=month, year=year)
    
    # lucky color
    lc = lucky_color(lpn=lpn)
    
    # generation
    gen = generation_checker(year=year)
    
    # print output
    print(f"\nYour birthday         : {birthday}")
    print(f"Your life path number : {lpn}")
    print(f"Your lucky color      : {lc}")
    print(f"Your generation       : {gen}")

# Global variables for testing
birthday = None
day = None
month = None
year = None
lpn = None
lc = None
gen = None

if __name__ == "__main__":
    main()