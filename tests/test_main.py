import unittest
import io
import sys
from unittest.mock import patch
import main
from src.validate_birthday import validate_birthday
from src.life_path_number import life_path_number
from src.lucky_color import lucky_color
from src.generation_checker import generation_checker

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='13 November 1987')
    def test_valid_input(self, mock_input):
        """Test with valid birthday input."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        main.birthday = mock_input()
        main.day, main.month, main.year = validate_birthday(birthday=main.birthday)
        main.lpn = life_path_number(day=main.day, month=main.month, year=main.year)
        main.lc = lucky_color(lpn=main.lpn)
        main.gen = generation_checker(year=main.year)
        
        # Print output
        print(f"\nYour birthday         : {main.birthday}")
        print(f"Your life path number : {main.lpn}")
        print(f"Your lucky color      : {main.lc}")
        print(f"Your generation       : {main.gen}")
        
        sys.stdout = sys.__stdout__
        self.assertIn("13 November 1987", captured_output.getvalue())
        self.assertIn("Your life path number", captured_output.getvalue())
        
    @patch('builtins.input', return_value='13 XX 1987')
    def test_invalid_input(self, mock_input):
        """Test with invalid birthday input."""
        with self.assertRaises(ValueError):
            main.birthday = mock_input()
            main.day, main.month, main.year = validate_birthday(birthday=main.birthday)