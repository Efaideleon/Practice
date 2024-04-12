import sys
sys.path.insert(0, '/Users/efaideleon/Documents/Efaideleon GitHub Repos/Practice/calculator_python')

import unittest
from main import CalculatorGUI

class CalculatorGUITest(unittest.TestCase):

    def test_addition(self):
        calculator_gui = CalculatorGUI()
        calculator_gui.first_number = 5
        calculator_gui.second_number = 3
        calculator_gui.operation = "1"
        calculator_gui.perform_calculation()
        self.assertEqual(calculator_gui.result, 8)

    def test_subtraction(self):
        calculator_gui = CalculatorGUI()
        calculator_gui.first_number = 10
        calculator_gui.second_number = 5
        calculator_gui.operation = "2"
        calculator_gui.perform_calculation()
        self.assertEqual(calculator_gui.result, 5)

    def test_multiplication(self):
        calculator_gui = CalculatorGUI()
        calculator_gui.first_number = 4
        calculator_gui.second_number = 6
        calculator_gui.operation = "3"
        calculator_gui.perform_calculation()
        self.assertEqual(calculator_gui.result, 24)

    def test_division(self):
        calculator_gui = CalculatorGUI()
        calculator_gui.first_number = 12
        calculator_gui.second_number = 4
        calculator_gui.operation = "4"
        calculator_gui.perform_calculation()
        self.assertEqual(calculator_gui.result, 3)

    def test_invalid_operation(self):
        calculator_gui = CalculatorGUI()
        calculator_gui.first_number = 1
        calculator_gui.second_number = 2
        calculator_gui.operation = "5"
        calculator_gui.perform_calculation()
        self.assertEqual(calculator_gui.result, None)

if __name__ == '__main__':
    unittest.main()
