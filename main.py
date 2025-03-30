# import modules
from src.validate_birthday import validate_birthday
from src.life_path_number import life_path_number
from src.lucky_color import lucky_color
from src.generation_checker import generation_checker

def main():
    # First birthday
    birthday1 = input("Enter your birthday (e.g., 09 July 2005 or 13 Nov 1987): ")
    # Validate first birthday
    day1, month1, year1 = validate_birthday(birthday=birthday1)
    # Calculate life path number for first birthday
    lpn1 = life_path_number(day=day1, month=month1, year=year1)
    # Find lucky color for first birthday
    lc1 = lucky_color(lpn=lpn1)
    # Check generation for first birthday
    gen1 = generation_checker(year=year1)
    
    # Print output for first birthday
    print(f"\nYour birthday : {birthday1}")
    print(f"Your life path number : {lpn1}")
    print(f"Your lucky color : {lc1}")
    print(f"Your generation : {gen1}")
    
    # Ask if user wants to compare with another birthday
    compare_option = input("\nDo you want to compare with another birthday? (yes/y): ").lower()
    
    if compare_option == "yes" or compare_option == "y":
        # Second birthday
        birthday2 = input("Enter second birthday (e.g., 09 July 2005 or 13 Nov 1987): ")
        # Validate second birthday
        day2, month2, year2 = validate_birthday(birthday=birthday2)
        # Calculate life path number for second birthday
        lpn2 = life_path_number(day=day2, month=month2, year=year2)
        # Find lucky color for second birthday
        lc2 = lucky_color(lpn=lpn2)
        # Check generation for second birthday
        gen2 = generation_checker(year=year2)
        
        # Print output for second birthday individually
        print(f"\nSecond birthday : {birthday2}")
        print(f"Life path number : {lpn2}")
        print(f"Lucky color : {lc2}")
        print(f"Generation : {gen2}")
        
        # Create side-by-side comparison box
        print("\n" + "=" * 50)
        print(f"{'COMPARISON':^50}")
        print("=" * 50)
        
        # Calculate column widths based on content
        # Left column (Person 1)
        p1_label = "Person 1"
        p1_birthday = f"Birthday: {birthday1}"
        p1_lpn = f"Life Path Number: {lpn1}"
        p1_lucky = f"Lucky Color: {lc1}"
        p1_gen = f"Generation: {gen1}"
        
        # Right column (Person 2)
        p2_label = "Person 2"
        p2_birthday = f"Birthday: {birthday2}"
        p2_lpn = f"Life Path Number: {lpn2}"
        p2_lucky = f"Lucky Color: {lc2}"
        p2_gen = f"Generation: {gen2}"
        
        # Find maximum width needed for each column
        col_width = 24  # Minimum width for each column
        
        # Print the comparison table
        print(f"{p1_label:^{col_width}} | {p2_label:^{col_width}}")
        print("-" * 50)
        print(f"{p1_birthday:<{col_width}} | {p2_birthday:<{col_width}}")
        print(f"{p1_lpn:<{col_width}} | {p2_lpn:<{col_width}}")
        print(f"{p1_lucky:<{col_width}} | {p2_lucky:<{col_width}}")
        print(f"{p1_gen:<{col_width}} | {p2_gen:<{col_width}}")
        print("-" * 50)
        
        # Compare life path numbers
        if lpn1 == lpn2:
            comparison_result = f"Same Life Path Number: {lpn1}"
        else:
            comparison_result = f"Different Life Path Numbers: {lpn1} vs {lpn2}"
        
        print(f"{comparison_result:^50}")
        print("=" * 50)

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