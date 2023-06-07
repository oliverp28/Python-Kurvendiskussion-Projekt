""" Importieren der Klasse linear_function. """
import linear_function


def test_typical():
    """
    Test für eine typische lineare Funktion.
    """
    test_func = "5x + 2"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 5
    assert lin_function.calculate_zeros() == -0.4
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_zero_multiply_with_positiv_end():
    """
    Test für eine Funktion mit einer 0 und einem positiven Ende.
    """
    test_func = "+ 0 * x + 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() is True
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_zero_multiply_with_negativ_end():
    """
    Test für eine Funktion mit einer 0 und einem negativen Ende.
    """
    test_func = "+ 0 * x - 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() is True
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_one_multiply_with_positive_end():
    """
    Test für eine Funktion mit einer 1 und einem positiven Ende.
    """
    test_func = "+ 1 * x + 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 1
    assert lin_function.calculate_zeros() == -1
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_one_negative_multiply_with_negative_end():
    """
    Test für eine Funktion mit einem negativen Multiplikator und einem negativen Ende.
    """
    test_func = "- 1 * x - 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == -1
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "fallend"


def test_one_negative_multiply_with_0_end():
    """
    Test für eine Funktion mit einem negativen Multiplikator und einer 0 am Ende.
    """
    test_func = "- 1 * x - 0"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is True
    assert lin_function.calculate_monotonicity() == "fallend"


def test_only_x():
    """
    Test für eine Funktion x.
    """
    test_func = "x"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is True
    assert lin_function.calculate_monotonicity() == "steigend"


def test_only_negative_x():
    """
    Test für eine Funktion mit einem negativen x.
    """
    test_func = "- x"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is True
    assert lin_function.calculate_monotonicity() == "fallend"


def test_only_one():
    """
    Test für eine Funktion mit einer 1.
    """
    test_func = "1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() is True
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_decimal_num_with_different_signs():
    """
    Test für eine Funktion mit einer Kommazahl und unterschiedliche Trennzeichen.
    """
    test_func = "0,5 * x + 1.0"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 0.5
    assert lin_function.calculate_zeros() == -2
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_only_decimal_num():
    """
    Test für eine Funktion mit Kommazahlen.
    """
    test_func = "0,1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() is True
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_high_value():
    """
    Test für eine Funktion mit hohen Werten.
    """
    test_func = "100x + 500"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 100
    assert lin_function.calculate_zeros() == -5
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_only_x_with_end():
    """
    Test für eine Funktion mit x und einem Ende.
    """
    test_func = "x + 2"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 1
    assert lin_function.calculate_zeros() == -2
    assert lin_function.calculate_symmetry_x() is False
    assert lin_function.calculate_point_symmetry_origin() is False
    assert lin_function.calculate_monotonicity() == "steigend"
