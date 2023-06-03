"""Class Quadratic_Func a part of curve discussion"""
from curve_discussion_output import Curve_Discussion_Output


class Quadratic_Func:
    """class that representates quadratic functions"""

    def __init__(self, input_func, *, _format=True):
        """Instanciate the input from the validation class

        Args:
            input (sequenz in special form): quadratic function
        """
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
                entry_list = input_func.split(", ")

            if len(entry_list) > 3:
                raise RuntimeError(
                    "Too much values, quadratic functions only take 3 inputs (ax**2, bx, c)"
                )

            for index, entry in enumerate(
                entry_list
            ):  # removing the x's to work with the numbers
                if index == 0:  # replace the x**2
                    if isinstance(
                        entry, str
                    ):  # if it is no string, it can't hold a x**2 in it
                        entry_list[index] = entry.replace("x**2", "")
                    if entry == "":  # when the entry is empty after the replacement,
                        # it will replace it with one, because x**2 == 1x**2
                        entry_list[index] = 1.0

                elif index == 1:  # replace the x
                    if isinstance(
                        entry, str
                    ):  # if it is no string, it can't hold a x in it
                        if "x" in entry:
                            entry_list[index] = entry.replace("x", "")
                            if entry == "":  # same as above x == 1x
                                entry_list[index] = 1.0
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
                raise RuntimeError("faulty input")
        self._func = tuple(entry_list)

    @property
    def y_intercept(self):
        """function that calculates the y_intercept, c == y_intercept"""
        return self._func[-1]

    @property
    def zeropoints(self):
        """function to searches all zeropoints of a quadratic function"""
        a_part = self._func[0]  # a (ax**2, bx, c)
        b_part = self._func[1]  # b
        c_part = self._func[2]  # c

        discriminant = b_part**2 - 4 * a_part * c_part
        if (discriminant) < 0:
            return None  # if the discriminant is negative, there are no zeropoints

        value1 = (-b_part + (discriminant) ** 0.5) / (2 * a_part)
        if (discriminant) == 0:  # if the discriminant is 0, there is only one zeropoint
            return value1 # tuple for the output class
        value2 = (-b_part - (discriminant) ** 0.5) / (2 * a_part)
        return value1, value2

    def __repr__(self):
        return "Quadratic_func(" + repr(self._func) + ")"

    def __iter__(self):
        return iter(self._func)

    def __eq__(self, other):
        if isinstance(other, Quadratic_Func):
            for x_entry, y_entry in zip(self._func, other._func):
                if x_entry != y_entry:
                    return False
            return True
        return False

    def __contains__(self, value):
        for entry in self._func:
            if abs(entry - value) < 0.000_000_1:
                return True
        return False

    def __pos__(self):
        return Quadratic_Func(self._func, _format=False)

    def __neg__(self):
        temp = [-x for x in self._func]
        return Quadratic_Func(temp, _format=False)

    def __add__(self, other):
        if isinstance(other, Quadratic_Func):  # add with 2 quadratic functions
            temp = [x + y for x, y in zip(self._func, other._func)]
            return Quadratic_Func(temp, _format=False)
        if isinstance(other, (int, float)):  # add numbers to c, known as y-axis shift
            temp = list(self._func)
            temp[-1] += other
            return Quadratic_Func(temp, _format=False)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
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
