import unittest
from src.generation_checker import generation_checker

class TestGenerationChecker(unittest.TestCase):
    # Equivalence Partitioning Tests
    def test_silent_generation(self):
        """Silent Generation year."""
        self.assertEqual(generation_checker(1940), "Silent Generation")
        
    def test_baby_boomers(self):
        """Baby Boomers year."""
        self.assertEqual(generation_checker(1960), "Baby Boomers")
        
    def test_generation_x(self):
        """Generation X year."""
        self.assertEqual(generation_checker(1970), "Generation X")
        
    def test_millennials(self):
        """Millennials year."""
        self.assertEqual(generation_checker(1990), "Millennials")
        
    def test_generation_z(self):
        """Generation Z year."""
        self.assertEqual(generation_checker(2000), "Generation Z")
        
    def test_generation_alpha(self):
        """Generation Alpha year."""
        self.assertEqual(generation_checker(2015), "Generation Alpha")
        
    def test_unknown_generation(self):
        """Year outside valid ranges."""
        self.assertEqual(generation_checker(1900), "Unknown")
    
    # Boundary Value Analysis Tests
    def test_start_silent_generation(self):
        """Start of Silent Generation."""
        self.assertEqual(generation_checker(1901), "Silent Generation")
        
    def test_end_silent_generation(self):
        """End of Silent Generation."""
        self.assertEqual(generation_checker(1945), "Silent Generation")
        
    def test_start_baby_boomers(self):
        """Start of Baby Boomers."""
        self.assertEqual(generation_checker(1946), "Baby Boomers")
        
    def test_end_baby_boomers(self):
        """End of Baby Boomers."""
        self.assertEqual(generation_checker(1964), "Baby Boomers")
        
    def test_start_generation_x(self):
        """Start of Generation X."""
        self.assertEqual(generation_checker(1965), "Generation X")
        
    def test_end_generation_x(self):
        """End of Generation X."""
        self.assertEqual(generation_checker(1979), "Generation X")
        
    def test_start_millennials(self):
        """Start of Millennials."""
        self.assertEqual(generation_checker(1980), "Millennials")
        
    def test_end_millennials(self):
        """End of Millennials."""
        self.assertEqual(generation_checker(1994), "Millennials")
        
    def test_start_generation_z(self):
        """Start of Generation Z."""
        self.assertEqual(generation_checker(1995), "Generation Z")
        
    def test_end_generation_z(self):
        """End of Generation Z."""
        self.assertEqual(generation_checker(2009), "Generation Z")
        
    def test_start_generation_alpha(self):
        """Start of Generation Alpha."""
        self.assertEqual(generation_checker(2010), "Generation Alpha")
        
    def test_end_generation_alpha(self):
        """End of Generation Alpha."""
        self.assertEqual(generation_checker(2024), "Generation Alpha")