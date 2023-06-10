"""Class Quadratic_Func a part of curve discussion"""
from curve_discussion_output import Curve_Discussion_Output


class Quadratic_Func:
    """class that representates quadratic functions"""

    def __init__(self,
                 function,
                 *,
                 _format=True):
        """
            Instanciate the input from the validation class

            Args:
                function (sequenz in special form): quadratic function
        """

        input_func = function

        entry_list = input_func

        if isinstance(entry_list, (tuple, list)):  # checking if formating is needed
            if len(entry_list) == 3:
                _format = False
                for (
                    check_entry
                ) in (
                    entry_list
                ):  # if one entry doesn't match the format, then _format gets activated
                    if not isinstance(check_entry, (int, float)):
                        _format = True

        if _format:
            if isinstance(
                input_func, str
            ):  # if the input is a string, it will split it into a list
                entry_list = input_func.split(",")

            if len(entry_list) > 3:
                raise RuntimeError(
                    "Zu viele Werte. Quadratische Funktionen akzeptieren nur 3 Eingaben (ax**2, bx, c)."
                )

            for index, entry in enumerate(
                entry_list
            ):  # removing the x's to work with the numbers
                if index == 0:  # replace the x**2
                    if isinstance(
                        entry, str
                    ):  # if it is no string, it can't hold a x**2 in it
                        entry_list[index] = entry_list[index].replace("x**2", "")
                        entry_list[index] = entry_list[index].replace("x^2", "")
                    if entry_list[index] == "":  # when the entry is empty after the replacement,
                        # it will replace it with one, because x**2 == 1x**2
                        entry_list[index] = 1.0
                    if entry_list[index] == "-":
                        entry_list[index] = -1.0

                elif index == 1:  # replace the x
                    if isinstance(
                        entry, str
                    ):  # if it is no string, it can't hold a x in it
                        if "x" in entry:
                            entry_list[index] = entry.replace("x", "")
                            if entry_list[index] == "":  # same as above x == 1x
                                entry_list[index] = 1.0
                            if entry_list[index] == "-":
                                entry_list[index] = -1.0
                            continue
                        if (
                            len(entry_list) == 2
                        ):  # if the second entry is not the bx, it must be the c
                            entry_list.insert(
                                index, 0.0
                            )  # therefore we extend the function with a 0
                            # between the ax**2 and the c to keep the format

                elif (
                    index == 2
                ):  # the c part doesn't need to be changed, so we will keep it in place
                    entry_list[index] = entry

            while (
                len(entry_list) != 3
            ):  # this loop only triggers when there is a not enough inputs, so it fills up with 0's
                entry_list.append(0.0)

            try:  # testing if every entry is a number
                for i, func_entry in enumerate(entry_list):
                    if not isinstance(func_entry, float):
                        entry_list[i] = float(func_entry)
            except ValueError:
                raise RuntimeError("Fehlerhafte Eingabe.")
        self._func = tuple(entry_list)
        self._a_part = self._func[0]  # a (ax**2, bx, c)
        self._b_part = self._func[1]  # b
        self._c_part = self._func[2]  # c
        self.output()

    @property
    def y_intercept(self):
        """function that calculates the y_intercept, c == y_intercept"""
        return self._func[-1]

    @property
    def zeropoints(self):
        """function to searches all zeropoints of a quadratic function"""
        discriminant = self._b_part**2 - 4 * self._a_part * self._c_part
        if (discriminant) < 0:
            return None  # if the discriminant is negative, there are no zeropoints

        value1 = (-self._b_part + (discriminant) ** 0.5) / (2 * self._a_part)
        if (discriminant) == 0:  # if the discriminant is 0, there is only one zeropoint
            return value1  # tuple for the output class
        value2 = (-self._b_part - (discriminant) ** 0.5) / (2 * self._a_part)
        return value1, value2

    @property
    def derivative(self):  # derivative is (2ax**1, b) c falls out
        """function to get the derivative of the quadratic function"""
        a_derivative = self._a_part * 2
        b_derivative = self._b_part
        return a_derivative, b_derivative

    @property
    def extremum(self):
        """function to get the extremum of the quadratic function"""
        a_temp, b_temp = self.derivative
        x_extremum = -b_temp / a_temp  # x point of the extremum
        y_extremum = (
            self._a_part * (x_extremum**2) + self._b_part * x_extremum + self._c_part
        )
        # inserts x coordinate for the y coordinate
        return x_extremum, y_extremum

    @property
    def symmetry_y_axis(self):
        """If True function is symmetrical to y-axis. b is for shift in x-dir, 0 means no shift"""
        return True if self._b_part == 0 else False

    def __repr__(self):
        return "Quadratic_func(" + repr(self._func) + ")"

    def __iter__(self):
        return iter(self._func)

    def __eq__(self,
               other):
        if isinstance(other, Quadratic_Func):
            for x_entry, y_entry in zip(self._func, other._func):
                if x_entry != y_entry:
                    return False
            return True
        return NotImplemented

    def __contains__(self,
                     value):
        for entry in self._func:
            if abs(entry - value) < 0.000_000_1:
                return True
        return False

    def __pos__(self):
        return Quadratic_Func(self._func, _format=False)

    def __neg__(self):
        temp = [-x for x in self._func]
        return Quadratic_Func(temp, _format=False)

    def __add__(self,
                other):
        if isinstance(other, Quadratic_Func):  # add with 2 quadratic functions
            temp = [x + y for x, y in zip(self._func, other._func)]
            return Quadratic_Func(temp, _format=False)
        if isinstance(other, (int, float)):  # add numbers to c, known as y-axis shift
            temp = list(self._func)
            temp[-1] += other
            return Quadratic_Func(temp, _format=False)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self,
                other):
        if isinstance(other, Quadratic_Func):  # subtracion with 2 quadratic functions
            temp = [x - y for x, y in zip(self._func, other._func)]
            return Quadratic_Func(temp, _format=False)
        if isinstance(
            other, (int, float)
        ):  # subtraction with numbers to c, known as y-axis shift
            temp = list(self._func)
            temp[-1] -= other
            return Quadratic_Func(temp, _format=False)
        return NotImplemented

    __rsub__ = __sub__

    def output(self):
        """ Formats the output. """
        Curve_Discussion_Output(function = Quadratic_Func.format_back(self).replace("- -", "- "),
                                function_type = "quad",
                                derivative = Quadratic_Func.format_back(self.derivative),
                                zeros_quad = self.zeropoints,
                                symmetry_y = self.symmetry_y_axis,
                                extremum = self.extremum
                                )

    @classmethod
    def format_back(cls,
                    func):
        """ Formats the output string. """
        output_string = ""
        if isinstance(func, Quadratic_Func): # checking how often we have to loop
            stopping_by = -4  # quadratic functions has a length of 3
            exporting_func = func._func
        if not isinstance(func, Quadratic_Func):
            stopping_by = -3  # derivative has a length of 2
            exporting_func = func

        for index in range(-1, stopping_by, -1):
            if index == -1: # starting with the c from the back
                if exporting_func[index] > 0:
                    output_string = " + " + str(abs(exporting_func[-1]))
                elif exporting_func[index] < 0:
                    output_string = " - " + str(abs(exporting_func[-1]))
                else: # if the c is 0 we skip it
                    continue

            if index == -2: # put the b with the x in front of the c
                temporary_string = str(exporting_func[-2]) + "x"
                if len(exporting_func) == 3:
                    if exporting_func[index] > 0:
                        temporary_string = " + " + temporary_string
                    elif exporting_func[index] < 0:
                        temporary_string = " - " + temporary_string
                    else: # if the b is 0 then it can be ignored
                        temporary_string = ""
                output_string = temporary_string + output_string

            if index == -3: # adding the a with x^2 at the front
                output_string = str(exporting_func[index]) + "x^2" + output_string
        return output_string
