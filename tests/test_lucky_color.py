import unittest
from src.lucky_color import lucky_color

class TestLuckyColor(unittest.TestCase):
    # Equivalence Partitioning Tests
    def test_regular_number(self):
        """Regular number (1-9)."""
        self.assertEqual(lucky_color(5), "Sky Blue")
        
    def test_master_number_11(self):
        """Master number 11."""
        self.assertEqual(lucky_color(11), "Silver")
        
    def test_master_number_22(self):
        """Master number 22."""
        self.assertEqual(lucky_color(22), "White")
        
    def test_master_number_33(self):
        """Master number 33."""
        self.assertEqual(lucky_color(33), "Crimson")