import unittest
from src.validate_birthday import validate_birthday

class TestValidateBirthday(unittest.TestCase):
    # Equivalence Partitioning Tests
    def test_valid_full_month(self):
        """Test valid birthday with full month name."""
        self.assertEqual(validate_birthday("13 November 1987"), (13, 11, 1987))
        
    def test_valid_month_abbreviation(self):
        """Test valid birthday with month abbreviation."""
        self.assertEqual(validate_birthday("13 Nov 1987"), (13, 11, 1987))
        
    def test_valid_numeric_month(self):
        """Test valid birthday with numeric month."""
        self.assertEqual(validate_birthday("13 11 1987"), (13, 11, 1987))
        
    def test_invalid_format(self):
        """Test invalid birthday format (missing components)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 1987")
            
    def test_invalid_day_non_numeric(self):
        """Test invalid day (non-numeric)."""
        with self.assertRaises(ValueError):
            validate_birthday("AA November 1987")
            
    def test_invalid_month_name(self):
        """Test invalid month (non-existent)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 Novem 1987")
            
    def test_invalid_year_non_numeric(self):
        """Test invalid year (non-numeric)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 November XXXX")
            
    def test_invalid_day_out_of_range(self):
        """Test invalid day (out of month range)."""
        with self.assertRaises(ValueError):
            validate_birthday("31 February 2000")
            
    def test_invalid_year_out_of_range(self):
        """Test invalid year (out of acceptance range)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 November 2026")
    
    # Boundary Value Analysis Tests
    def test_earliest_valid_year(self):
        """Test earliest valid year."""
        self.assertEqual(validate_birthday("01 January 1925"), (1, 1, 1925))
        
    def test_latest_valid_year(self):
        """Test latest valid year."""
        self.assertEqual(validate_birthday("31 December 2025"), (31, 12, 2025))
        
    def test_below_earliest_valid_year(self):
        """Test just below earliest valid year."""
        with self.assertRaises(ValueError):
            validate_birthday("31 December 1924")
            
    def test_above_latest_valid_year(self):
        """Test just above latest valid year."""
        with self.assertRaises(ValueError):
            validate_birthday("01 January 2026")
            
    def test_minimum_valid_day(self):
        """Test minimum valid day."""
        self.assertEqual(validate_birthday("01 January 2000"), (1, 1, 2000))
        
    def test_maximum_valid_day(self):
        """Test maximum valid day (31-day month)."""
        self.assertEqual(validate_birthday("31 January 2000"), (31, 1, 2000))
        
    def test_above_maximum_day(self):
        """Test just above maximum day (31-day month)."""
        with self.assertRaises(ValueError):
            validate_birthday("32 January 2000")
            
    def test_leap_year_feb_29(self):
        """Test February 29 on leap year."""
        self.assertEqual(validate_birthday("29 February 2000"), (29, 2, 2000))
        
    def test_non_leap_year_feb_29(self):
        """Test February 29 on non-leap year."""
        with self.assertRaises(ValueError):
            validate_birthday("29 February 1999")
    
    # White-Box Tests
    def test_wb_valid_numeric_month(self):
        """Valid input format with numeric month."""
        self.assertEqual(validate_birthday("13 11 1987"), (13, 11, 1987))
        
    def test_wb_valid_month_name(self):
        """Valid input with month name."""
        self.assertEqual(validate_birthday("13 November 1987"), (13, 11, 1987))
        
    def test_wb_valid_month_abbreviation(self):
        """Valid input with month abbreviation."""
        self.assertEqual(validate_birthday("13 Nov 1987"), (13, 11, 1987))
        
    def test_wb_invalid_format(self):
        """Invalid format (too few components)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 1987")
            
    def test_wb_invalid_day(self):
        """Invalid day (non-numeric)."""
        with self.assertRaises(ValueError):
            validate_birthday("XX November 1987")
            
    def test_wb_invalid_month(self):
        """Invalid month (non-existent)."""
        with self.assertRaises(ValueError):
            validate_birthday("13 Xyz 1987")
            
    def test_wb_feb_29_leap_year(self):
        """February 29 in leap year."""
        self.assertEqual(validate_birthday("29 February 2000"), (29, 2, 2000))
        
    def test_wb_feb_29_non_leap_year(self):
        """February 29 in non-leap year."""
        with self.assertRaises(ValueError):
            validate_birthday("29 February 1999")