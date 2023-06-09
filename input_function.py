"""Index des ersten Auftretens von "-"""""
import linear_function
import quadratic_function

class Input_Function:
    """Import class quadratic_function"""
    def __init__(self):
        """
            Initialize Input_Function object.
        """

        validationBool = False

        self.create_header()

        while validationBool == False:
            function = self.get_function()
            if self.validate_input(function) == True: # Validate the input function
                if self.which_function(function) == True: # Determine the type of function
                    print("\n")
                    againBool = ""
                    while againBool != "ja" and againBool != "nein":
                        againBool = input("Willst du eine weitere Funktion eingeben ? (ja / nein):  ").lower()
                    if againBool == "nein":
                        validationBool = True
                    else:
                        self.create_header()

    def create_header(self):
        """Creates a header to increase usability."""

        print("\n")
        print("╔════════════════ EINGABE FORMAT ════════════════╗")
        print("║  QUAD: 3x^2 + 3 oder 4x**2 - 4    LIN: 3x - 3  ║")
        print("╚════════════════════════════════════════════════╝")

    def get_function(self):
        """
            Creates input field.
        """

        print("\n")
        function = input("Gib deine Funktion ein: f(x) = ")
        print("Du hast folgende Funktion eingegeben:", function)

        return function

    def validate_input(self,
                       function):
        """
            Validate the input function.

            Args:
                function (str): The input function to validate.
        """
        # Check for invalid cases
        invalid_cases = ["/x", "x/", "*x", "x* ", "^x", "x^ ", "x** "]
        for case in invalid_cases:
            if case in function:
                print("Ungültige Eingabe: " + case + "     ||      ungültige Fälle: '/x' | 'x/' | '*x' | 'x* ' | '^x' | 'x^ ' | 'x** '")
                return False

        allowed_characters = set("1234567890^*+- xX,.")

        for char in function:
            if char not in allowed_characters:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.     ||      gültige Zeichen: '1234567890^*+- xX,.'")
                return False

        return True

    def which_function(self,
                       function):
        """
            Determine the type of function.

            Args:
                function (str): The input function to analyze.
        """
        # Remove whitespace from the input function
        function = function.replace(" ", "")

        if function == "":
            # If no function is specified, raise an error
            raise ValueError("Bitte geben Sie eine Funktion an.")

        if "," in function:
            # If the input contains a comma, it will be replaced by a point
            function = function.replace(",", ".")

        if "x^" in function or "x**" in function:
            if "x^2" in function:
                checkIndex = function.index("^") + 2
                if (checkIndex + 1) <= len(function) and function[checkIndex].isdigit():
                    print("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.")
                else:
                    # If the input contains "x^2", it's a quadratic function
                    self.validate_quadratic_function(function)
                    quadratic_function.Quadratic_Func(self.split_function_quad(
                        function=function.lower()))  # Create a Quadratic_Function instance with lowercase x
                    return True
            elif "x**2" in function:
                checkIndex = function.index("*") + 3
                if (checkIndex + 1) <= len(function) and function[checkIndex].isdigit():
                    print("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.")
                else:
                    # If the input contains "x*2", it's a quadratic function
                    self.validate_quadratic_function(function)
                    quadratic_function.Quadratic_Func(self.split_function_quad(
                        function=function.lower()))  # Create a Quadratic_Function instance with lowercase x
                    return True
            else:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.")
        elif "x" in function or "x" not in function and "^" not in function and "**" not in function:
            # If the input contains "x" but doesn't have "^", it's a linear function
            self.validate_linear_function(function)
            linear_function.Linear_Func(function.lower())  # Create a Linear_Function instance with lowercase x
            return True
        else:
            # If none of the conditions above are met, it's an invalid input for a function
            print("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.")

    def validate_linear_function(self,
                                 function):
        """
            Validate a linear function.

            Args:
                function (str): The input function to validate.

            Raises:
                ValueError: If the linear function is invalid.
        """
        # Check for invalid cases in linear function

        if function.count("x") > 1:
            print("Ungültige Eingabe. Lineare Funktionen sollten nur einen Term mit 'x' enthalten.")

    def validate_quadratic_function(self,
                                    function):
        """
            Validate a quadratic function.

            Args:
                function (str): The input function to validate.
        """

        # Check for invalid cases in quadratic function
        if function.count("x^2") > 1 or function.count("x**2") > 1:
            print("Ungültige Eingabe. Quadratische Funktionen sollten nur einen Term mit 'x^2' enthalten.")

        if function.count("x") > 2:
            print("Ungültige Eingabe. Quadratische Funktionen sollten höchstens zwei Terme mit 'x' enthalten.")

    def split_function_quad(self,
                            function):
        """
            Preparation of the input for the quadratic function in Python.

            Args:
                function (str): The input function to validate.
        """

        if "+" in function:
            function = function.replace(" ", "")
            function = function.replace("+", ",")

        if "-" in function and function.index("-") < function.index("x") and function.count("-") == 1:
            function = function.replace(" ", "")

        elif "-" in function and function.index("-") > function.index("x") and function.count("-") == 1:
            function = function.replace("-", ",-")

        elif "-" in function and function.index("-") < function.index("x") and function.count("-") == 2:
            function = function.replace(" ", "")

            first_dash_index = function.find("-")  # index of the first "-"
            second_dash_index = function.find("-", first_dash_index + 1)  # index of the second "-"

            function = function[:second_dash_index] + ",-" + function[second_dash_index + 1:]

        elif "-" in function and function.index("-") < function.index("x") and function.count("-") == 3:
            function = function.replace(" ", "")

            first_dash_index = function.find("-")  # index of the first "-"
            second_dash_index = function.find("-", first_dash_index + 1)  # index of the second "-"
            third_dash_index = function.find("-", second_dash_index + 1)  # index of the second "-"

            function = function[:second_dash_index] + ",-" + function[second_dash_index + 1:]
            function = function[:third_dash_index] + "," + function[third_dash_index + 1:]
            print(function)

        return function
