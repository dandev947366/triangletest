import unittest
from main import classify_triangle 

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(7, 7, 7), "Equilateral triangle")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles triangle")

    def test_isosceles_triangle_invalid_third_side(self):
        self.assertEqual(classify_triangle(8, 8, 17), "Error: invalid input data value")

    def test_invalid_triangle_zero_length(self):
        self.assertEqual(classify_triangle(0, 10, 10), "Error: invalid input data value")

    def test_invalid_triangle_negative_lengths(self):
        self.assertEqual(classify_triangle(-1, -1, -1), "Error: invalid input data value")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene triangle")

    def test_invalid_triangle_sum_check(self):
        self.assertEqual(classify_triangle(1, 3, 1), "Error: invalid input data value")
    def test_isosceles_triangle_large_values(self):
        self.assertEqual(classify_triangle(999999.99, 999999.99, 999999.98), "Isosceles triangle")

    def test_isosceles_triangle_just_below_valid(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles triangle")

    def test_invalid_triangle_just_above_valid(self):
        self.assertEqual(classify_triangle(1, 2, 4), "Error: invalid input data value")
    def test_zero_value(self):
            self.assertEqual(classify_triangle(0, 5, 7), "Error: invalid input data value")   
        
    def test_negative_value(self):
        self.assertEqual(classify_triangle(-1, 5, 7), "Error: invalid input data value")
    def test_zero_value(self):
        self.assertEqual(classify_triangle(0, 5, 7), "Error: invalid input data value")    
    def test_inconsistent_data_type(self):
        self.assertEqual(classify_triangle(1, 2.5, 3), "Scalene triangle")
    def test_invalid_non_numeric_multiple_inputs(self):
        self.assertEqual(classify_triangle("a", "b", "c"), "Error: invalid input data value")
 

        
        
if __name__ == "__main__":
    unittest.main()
