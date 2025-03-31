import unittest
from pydantic import ValidationError
from models import Mortgage,MortgageInput
from credit_rating import calculate_credit_rating 
from test_data import VALID_MORTGAGES, EDGE_CASES, INVALID_MORTGAGES , AAA_MORTGAGES , BBB_MORTGAGES , C_MORTGAGES

class TestMortgageValidation(unittest.TestCase):
    
    def test_valid_mortgages(self):
        """Test that valid mortgage data passes validation."""
        mortgage_input = MortgageInput(**VALID_MORTGAGES)
        self.assertIsInstance(mortgage_input,MortgageInput)
    
    def test_edge_cases(self):
        """Test edge cases to ensure proper handling of boundary values."""
        mortgage_input = MortgageInput(**EDGE_CASES)
        self.assertIsInstance(mortgage_input,MortgageInput)
    
    def test_invalid_mortgages(self):
        """Test invalid mortgage data to ensure proper validation errors."""
        for data in INVALID_MORTGAGES["mortgages"]:
            with self.assertRaises(ValidationError):
                Mortgage(**data)

class TestCreditRating(unittest.TestCase):
    
    def test_credit_rating_high_score(self):
        """Test that high credit score results in a good rating."""
        self.assertEqual(calculate_credit_rating(MortgageInput(**AAA_MORTGAGES)), "AAA")
    
    def test_credit_rating_medium_score(self):
        """Test that a medium credit score gives a moderate rating."""
        self.assertEqual(calculate_credit_rating(MortgageInput(**BBB_MORTGAGES)),"BBB")
    
    def test_credit_rating_low_score(self):
        """Test that a low credit score leads to a lower rating."""
        self.assertEqual(calculate_credit_rating(MortgageInput(**C_MORTGAGES)), "C")
    
    def test_edge_cases_credit_rating(self):
        """Test edge cases """
        mortgage_input = MortgageInput(**EDGE_CASES)
        expected_rating = calculate_credit_rating(mortgage_input)
        self.assertIn(expected_rating,["AAA","BBB","CCC"])    
    
if __name__ == "__main__":
    unittest.main()
