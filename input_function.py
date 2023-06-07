from linear_function import Linear_Function
from quadratic_function import Quadratic_Function

class Input_Function:
    def __init__(self, function):
        """
        Get and validate input function
        """
        self.validate_input(function)
        self.which_function(function)

    def validate_input(self, function):
        # Check for invalid cases
        invalid_cases = ["/x", "x/", "*x", "x*"]
        for case in invalid_cases:
            if case in function:
                raise ValueError("Invalid input. Please use the correct format: 1/5x; 5/2x; 25x")

    def which_function(self, function):
        # Remove whitespace from the input function
        function = function.replace(" ", "")

        if function == "":
            # If no function is specified, raise an error
            raise ValueError("Please specify a function")

        if "," in function:
            # If the input contains a comma, it's an invalid input for decimal separator
            raise ValueError("Invalid input. Please enter the number with a dot as decimal separator")

        if any(symbol.isdigit() for symbol in function):
            # If the input contains a symbol number, it's an invalid input
            raise ValueError("Invalid input. Symbol numbers are not allowed. Please use the correct format: 1/5x; 5/2x; 25x")

        try:
            if "x^2" in function:
                # If the input contains "x^2", it's a quadratic function
                Quadratic_Function()
            elif "x" in function and "^" not in function:
                # If the input contains "x" but doesn't have "^", it's a linear function
                Linear_Function()
            else:
                # If none of the conditions above are met, it's an invalid input for a function
                raise ValueError("This input is incorrect. Please specify a valid function")
        except ValueError as e:
            print(e)


def validation():
    try:
        # Get the function from the user
        function = input("f(x) = ")

        # Create an instance of Input_Function to validate the input
        input_func = Input_Function(function)
    except ValueError as e:
        print(e)


validation()
