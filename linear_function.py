""" Import of the curve_discussion_output class. """
import curve_discussion_output


class Linear_Func:
    """
    Performs a curve discussion of a linear function.

    Components:
        - Derivative
        - Zeros to the x-axis
        - Symmetry to the x-axis
        - Symmetry to the origin
        - Monotonicity
    """

    def __init__(self, function):

        """
        arg:
            -> The input is a string representing a linear function
            -> Function format: a * x + b
            --> a represents the coefficient of x in the function
            --> b represents the constant term (anything after x)

            -> Allowed variations: + or - ax + or - b
                --> The * between a and x can be omitted, but it is not required
                --> Spacing rules do not matter
            -> Not allowed inputs:
                --> x/a
                --> a/x
                --> ax / b
                --> ax * b
        """

        self.function = self.validate_function(
            function
        )  # function, used as a class variable

        curve_discussion_output.Curve_Discussion_Output(
            function=function,
            function_type="lin",
            derivative=self.calculate_derivative(),
            zero_lin=self.calculate_zeros(),
            symmetry_x=self.calculate_symmetry_x(),
            symmetry_origin=self.calculate_point_symmetry_origin(),
            monotonicity=self.calculate_monotonicity(),
        )

    def validate_function(self, function):
        """
        Validation of the entered function

        args:
            function (str): The string representing the linear function
        returns:
            str: The validated function
        """
        function = function.replace(" ", "")  # removing spaces
        function = function.replace(",", ".")  # standardizing , to .
        function = function.replace(
            "*", ""
        )  # removing of * for cases like: 5*x to 5x for better computation
        if function.endswith("x"):  # adding + 0 for functions like 5x for analysis of b
            function += "+0"

        return function

    def parse_function(self):
        """
        Analyzing the function into its individual components

        args:
            function (str): The string representing the linear function

        returns:
            a: Function part up to and including x
            b: Function part from x to the end
            replace_a: Control variable for analyzing rare cases
        """
        function = self.function
        a_variable = ""  # Variable instantiation
        b_variable = ""
        replace_x = ""  # Control variable for functions like f(x) = x
        found_x = False

        for char in function:  # Checking if x is present
            if char == "x":
                found_x = True  # If x is present:
                a_variable += (
                    char  # the part up to and including x is loaded into variable a
                )
                break
            else:
                a_variable += char

        if found_x:
            b_variable = function[len(a_variable) :]  # Based on the length of a,
            # everything from the position immediately after a is loaded into variable b
        else:
            b_variable = (
                function  # If x is not present, everything is loaded into variable b
            )
            a_variable = ""

        if "x" in a_variable:  # Removing x from a to enable mathematical calculations
            a_variable = a_variable.replace("x", "")
            replace_x = True  # This control variable is involved in
                              # conditional statements or case distinctions
        else:
            replace_x = False

        if (
            a_variable == "+" or a_variable == "-"
        ):  # If x is present and in the case of +x or -x, a value of 1 is assigned to x
            a_variable += "1"

        return a_variable, b_variable, replace_x

    def calculate_derivative(self):
        """
        Calculation of the derivative

        args:
            Usage of the components of the function as strings: a, b, and replace_a
        returns:
            derivative: int; float; string (data type depends on the linear function)
        """
        a_variable, _, replace_x = self.parse_function()

        if (
            len(a_variable) == 0 and replace_x is False
        ):  # Test for the case when there is no slope, such as f(x) = 5
            derivative = "Keine Ableitung möglich."
            return derivative

        if (
            len(a_variable) == 0 and replace_x is True
        ):  # Test for the case when the function is f(x) = x
            derivative = 1
            return derivative

        a_variable = eval(a_variable)  # Conversion of +0 or -0 to 0

        if a_variable == 0:  # Test for the case when the function is f(x) = 0x + 2
            derivative = "Keine Ableitung möglich."
        else:
            derivative = a_variable

        return derivative

    def calculate_zeros(self):
        """
        Calculation of the zeros.

        args:
            Usage of the components of the function as strings: a, b, and replace_a
        returns:
            zero: int; float; string (data type depends on the linear function)
        """
        a_variable, b_variable, replace_x = self.parse_function()

        if len(a_variable) == 0:  # Test for f(x) = x
            if replace_x is True and eval(b_variable) == 0:
                zero = 0
                return zero

            if replace_x is True and eval(b_variable) != 0:  # Test for f(x) = x + 1
                zero = -eval(b_variable) / 1                 # Calculation of the zeros with a = 1
                return zero

            elif replace_x is False:  # Test for the case of a not existing a
                zero = "Keine Nullstelle vorhanden."
                return zero

        if eval(a_variable) == 0:  # Test for the case f(x) = -0x + 5
            zero = "Keine Nullstelle vorhanden."
            return zero

        if replace_x is True and b_variable == "0":  # Test for the case f(x) = 5x
            zero = 0
            return zero

        if len(a_variable) >= 1:  # Test for the case f(x) = 5x + 10
            zero = -eval(b_variable) / eval(a_variable)
            return zero

    def calculate_symmetry_x(self):

        """
        Determining symmetry to the x-axis

        args:
            Using the components of the function
            as strings: a, b, and replace_a
        returns:
            symmetrie_x: bool
        """

        a_variable, b_variable, replace_x = self.parse_function()

        if (
            a_variable == "" or eval(a_variable) == 0 and eval(b_variable) != 0
        ):  # Tests for a = 0 and b != 0
            symmetry_x = True
            if a_variable == "" and replace_x is True:  # Test for a != 0x
                symmetry_x = False

        else:  # Test when a != 0x
            symmetry_x = False

        return symmetry_x

    def calculate_point_symmetry_origin(self):

        """
        Determining symmetry to the origin

        args:
            Using the components of the function as a string in variable b
        returns:
            point_symmetrie_origin: bool
        """

        _, b_variable, _ = self.parse_function()
        b_variable = eval(b_variable)
        if b_variable == 0:  # Test if b equals 0
            point_symmetry_origin = True
        else:
            point_symmetry_origin = (
                False  # Applies to all cases when != 0 wie f(x) = 5x + 2
            )

        return point_symmetry_origin

    def calculate_monotonicity(self):

        """
        Determining the monotonicity

        args:
            Using the components of the function as a string in variable b
        returns:
            monotonicity: string
        """
        a_variable, _, replace_x = self.parse_function()

        if a_variable == "":  # x Apologies for the truncation
                              # In the case of f(x) = x, this scenario is being handled here
            if replace_x is True:
                monotonicity = "steigend"
            else:
                monotonicity = "konstant"  # Testing the case when there is
                                           # no slope present in variable a
        else:
            a_variable = eval(
                a_variable
            )  # Testing whether a is equal to 0, greater than 0, or less than 0
            if a_variable > 0:
                monotonicity = "steigend"
            elif a_variable < 0:
                monotonicity = "fallend"
            else:
                monotonicity = "konstant"

        return monotonicity
