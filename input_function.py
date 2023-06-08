""""""
import linear_function
import quadratic_function

class Input_Function:
    def __init__(self):
        """
            Initialize Input_Function object.

            Args:
                function (str): The input function to validate.

            Raises:
                ValueError: If the input function is invalid.
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
        """

        """

        print("\n")
        print("╔════════════════ EINGABE FORMAT ════════════════╗")
        print("║  QUAD: 3x^2 + 3 oder 4x**2 - 4    LIN: 3x - 3  ║")
        print("╚════════════════════════════════════════════════╝")

    def get_function(self):
        """

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

            Raises:
                ValueError: If the input function is invalid.
        """
        # Check for invalid cases
        invalid_cases = ["/x", "x/", "*x", "x* ", "^x", "x^ "]
        for case in invalid_cases:
            if case in function:
                raise ValueError("Ungültige Eingabe: " + case)

        return True

    def which_function(self,
                       function):
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
            raise ValueError("Bitte geben Sie eine Funktion an.")

        if "," in function:
            # If the input contains a comma, it will be replaced by a point
            function = function.replace(",", ".")

        try:
            if "x^2" in function or "x**2" in function:
                # If the input contains "x^2", it's a quadratic function
                self.validate_quadratic_function(function)
                quadratic_function.Quadratic_Func(self.split_function_quad(
                    function=function.lower()))  # Create a Quadratic_Function instance with lowercase x
                return True
            elif "x" in function and "^" not in function:
                # If the input contains "x" but doesn't have "^", it's a linear function
                self.validate_linear_function(function)
                linear_function.Linear_Func(function.lower())  # Create a Linear_Function instance with lowercase x
                return True
            else:
                # If none of the conditions above are met, it's an invalid input for a function
                raise ValueError("Ungültige Eingabe. Bitte geben Sie eine gültige Funktion an.")
        except ValueError as e:
            print(e)

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
            raise ValueError("Ungültige Eingabe. Lineare Funktionen sollten nur einen Term mit 'x' enthalten.")

        if "x" not in function:
            raise ValueError("Ungültige Eingabe. Lineare Funktionen sollten den Term 'x' enthalten.")

    def validate_quadratic_function(self,
                                    function):
        """
            Validate a quadratic function.

            Args:
                function (str): The input function to validate.

            Raises:
                ValueError: If the quadratic function is invalid.
        """

        # Check for invalid cases in quadratic function
        if function.count("x^2") > 1 or function.count("x**2") > 1:
            raise ValueError("Ungültige Eingabe. Quadratische Funktionen sollten nur einen Term mit 'x^2' enthalten.")

        if function.count("x") > 2:
            raise ValueError("Ungültige Eingabe. Quadratische Funktionen sollten höchstens zwei Terme mit 'x' enthalten.")

    def split_function_quad(self,
                            function):
        """

        """

        if "+" in function:
            function = function.replace(" ", "")
            function = function.replace("+", ", ")

        if "-" in function:
            function = function.replace(" ", "")
            function = function.replace("-", ", -")

        return function
