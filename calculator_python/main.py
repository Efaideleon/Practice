class Calculator:
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

class CalculatorGUI:
    calculator = Calculator()
    first_number = None
    second_number = None
    operation = None
    result = None

    def get_user_input(self):
        try: 
            self.first_number = input("Enter first number: ")
            self.second_number = input("Enter second number: ")
            self.operation = input("Enter operation (1: +, 2: -, 3: *, 4: /): ")  
        except ValueError as e:
            print("Error: Invalid input. Please enter a valid number", e)

    # Perform the calculation based on the user's input
    def perform_calculation(self):
        try:
            if self.operation == "1":
                self.result = self.calculator.addition(float(self.first_number), float(self.second_number))
            elif self.operation == "2":
                self.result = self.calculator.subtraction(float(self.first_number), float(self.second_number))
            elif self.operation == "3":
                self.result = self.calculator.multiplication(float(self.first_number), float(self.second_number))
            elif self.operation == "4":
                self.result = self.calculator.division(float(self.first_number), float(self.second_number))
            else:
                print("Invalid operation. Please enter a valid operation (1: +, 2: -, 3: *, 4: /).")
        except ValueError as e:
            print("Error: ", e)

    # Display the result to the user
    def display_result(self):
        print("The result is:", self.result)

    def run(self):
        self.get_user_input()
        self.perform_calculation()
        self.display_result()