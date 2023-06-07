from linear_function import Linear_Function
from quadratic_function import Quadratic_Function

class Input_Function:
    def __init__(self, function):
        """
        Initialize Input_Function object.

        Args:
            function (str): The input function to validate.

        Raises:
            ValueError: If the input function is invalid.
        """
        self.validate_input(function)  # Validate the input function
        self.which_function(function)  # Determine the type of function

    def validate_input(self, function):
        """
        Validate the input function.

        Args:
            function (str): The input function to validate.

        Raises:
            ValueError: If the input function is invalid.
        """
        # Check for invalid cases
        invalid_cases = ["/x", "x/", "*x", "x*", "^x", "x^"]
        for case in invalid_cases:
            if case in function:
                raise ValueError("Invalid input " + case)

    def validate_linear_function(self, function):
        """
        Validate a linear function.

        Args:
            function (str): The input function to validate.

        Raises:
            ValueError: If the linear function is invalid.
        """
        # Check for invalid cases in linear function
        if "x^" in function or "^x" in function:
            raise ValueError("Invalid input. Linear functions should not contain '^'")

        if function.count("x") > 1:
            raise ValueError("Invalid input. Linear functions should have only one 'x' term")

        if any(symbol.isdigit() for symbol in function):
            raise ValueError("Invalid input. Symbol numbers are not allowed. Please use the correct format.)

        if "x" not in function:
            raise ValueError("Invalid input. Linear functions should contain the term 'x'")

    def validate_quadratic_function(self, function):
        """
        Validate a quadratic function.

        Args:
            function (str): The input function to validate.

        Raises:
            ValueError: If the quadratic function is invalid.
        """
        # Check for invalid cases in quadratic function
        if function.count("x^2") > 1:
            raise ValueError("Invalid input. Quadratic functions should have only one 'x^2' term")

        if function.count("x") > 2:
            raise ValueError("Invalid input. Quadratic functions should have at most two 'x' terms")

        if any(symbol.isdigit() for symbol in function):
            raise ValueError("Invalid input. Symbol numbers are not allowed. Please use the correct format")

        if "x^2" not in function:
            raise ValueError("Invalid input. Quadratic functions should contain the term 'x^2'")

    def which_function(self, function):
        """
        Determine the type of function.

        Args:
            function (str): The input function to analyze.

        Raises:
            ValueError: If the input function is not a valid function.
        """
        # Remove whitespace from the input function
        function = function.replace(" ", "")

        if function == "":
            # If no function is specified, raise an error
            raise ValueError("Please specify a function")

        if "," in function:
            # If the input contains a comma, it's an invalid input for decimal separator
            raise ValueError("Invalid input. Please enter the number with a dot as decimal separator")

        try:
            if "x^2" in function:
                # If the input contains "x^2", it's a quadratic function
                self.validate_quadratic_function(function)
                Quadratic_Function(function.lower())  # Create a Quadratic_Function instance with lowercase x
            elif "x" in function and "^" not in function:
                # If the input contains "x" but doesn't have "^", it's a linear function
                self.validate_linear_function(function)
                Linear_Function(function.lower())  # Create a Linear_Function instance with lowercase x
            else:
                # If none of the conditions above are met, it's an invalid input for a function
                raise ValueError("Invalid input. Please specify a valid function")
        except ValueError as e:
            print(e)

def validation():
    """
    Validate the input function provided by the user.
    """
    try:
        # Get the function from the user
        function = input("f(x) = ")

        # Create an instance of Input_Function to validate the input
        input_func = Input_Function(function)
    except ValueError as e:
        print(e)

validation()
