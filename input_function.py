from linear_function import Linear_Function
from quadratic_function import Quadratic_Function

class Input_Function:

    def __init__(self, function):
        """
            get and validate input function
        """
        def which_function(function):
    # Remove whitespace from the input function
    function = function.replace(" ", "")

    if function == "":
        # If no function is specified, print an error message
        print("Please specify a function")

    elif "," in function:
        # If the input contains a comma, it's an invalid input for decimal separator
        print("Invalid input. Please enter the number with a dot as decimal separator")

    elif "x^2" in function:
        # If the input contains "x^2", it's a quadratic function
        return "quadratic"

    elif "x" in function:
        if "^" not in function:
            # If the input contains "x" but doesn't have "^", it's a linear function
            return "linear"

    else:
        # If none of the conditions above are met, it's an invalid input for a function
        return "This input is incorrect. Please specify a valid function"


def validation():
    # Get the function from the user
    function = input("f(x) = ")

    # Determine the type of function using the which_function function
    function_type = which_function(function)

    if function_type == "quadratic":
        # Call the Quadratic Func
        Quadratic_Func.__init__()

    elif function_type == "linear":
        # Call the Linear_Func() function or class to handle linear functions
        Linear_Func.__init__()

    else:
        # If the function type is neither quadratic nor linear, print an error message
        print("This input is incorrect. Please specify a valid function")


validation()
        
        
        self.get_function()

    def get_function(self):

        function = input("Gib deine Funktion ein: ")
        print("Du hast folgende Funktion eingegeben:", function)
