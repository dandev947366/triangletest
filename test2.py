import unittest
from main import classify_triangle 

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        # Arrange
        side1, side2, side3 = 7, 7, 7
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Equilateral triangle")

    def test_isosceles_triangle(self):
        # Arrange
        side1, side2, side3 = 5, 5, 3
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Isosceles triangle")

    def test_isosceles_triangle_invalid_third_side(self):
        # Arrange
        side1, side2, side3 = 8, 8, 17
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

    def test_invalid_triangle_zero_length(self):
        # Arrange
        side1, side2, side3 = 0, 10, 10
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

    def test_invalid_triangle_negative_lengths(self):
        # Arrange
        side1, side2, side3 = -1, -1, -1
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

    def test_scalene_triangle(self):
        # Arrange
        side1, side2, side3 = 3, 4, 5
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Scalene triangle")

    def test_invalid_triangle_sum_check(self):
        # Arrange
        side1, side2, side3 = 1, 3, 1
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

    def test_isosceles_triangle_large_values(self):
        # Arrange
        side1, side2, side3 = 999999.99, 999999.99, 999999.98
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Isosceles triangle")

    def test_invalid_triangle_just_above_valid(self):
        # Arrange
        side1, side2, side3 = 1, 2, 4
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

    def test_inconsistent_data_type(self):
        # Arrange
        side1, side2, side3 = 1, 2.5, 3
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Scalene triangle")

    def test_invalid_non_numeric_multiple_inputs(self):
        # Arrange
        side1, side2, side3 = "a", "b", "c"
        
        # Act
        result = classify_triangle(side1, side2, side3)
        
        # Assert
        self.assertEqual(result, "Error: invalid input data value")

if __name__ == "__main__":
    unittest.main()
