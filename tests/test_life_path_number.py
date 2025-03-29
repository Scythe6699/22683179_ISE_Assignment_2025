import unittest
from src.life_path_number import life_path_number

class TestLifePathNumber(unittest.TestCase):
    # Equivalence Partitioning Tests
    def test_basic_calculation(self):
        """Basic calculation with single-digit result."""
        self.assertEqual(life_path_number(1, 1, 2000), 4)
        
    def test_reduction_needed(self):
        """Calculation with reduction needed."""
        self.assertEqual(life_path_number(29, 8, 1994), 6)
        
    def test_master_number_result(self):
        """Calculation with master number result."""
        self.assertEqual(life_path_number(29, 2, 1980), 22)
        
    def test_master_number_input(self):
        """Calculation with master number input."""
        self.assertEqual(life_path_number(11, 3, 1986), 2)
        
    def test_multiple_master_numbers(self):
        """Calculation with multiple master numbers."""
        self.assertEqual(life_path_number(11, 11, 2000), 6)
    
    # White-Box Tests
    def test_wb_single_digit(self):
        """Single-digit number path."""
        self.assertEqual(life_path_number(1, 1, 2000), 4)
        
    def test_wb_master_number_input(self):
        """Master number input path."""
        self.assertEqual(life_path_number(11, 5, 2000), 9)
        
    def test_wb_master_number_output(self):
        """Master number output path."""
        self.assertEqual(life_path_number(29, 2, 1980), 22)
        
    def test_wb_recursive_addition(self):
        """Recursive digit addition path."""
        self.assertEqual(life_path_number(29, 12, 1994), 1)
        
    def test_wb_multiple_masters_input(self):
        """Multiple master numbers input."""
        self.assertEqual(life_path_number(11, 22, 1987), 4)
