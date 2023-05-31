import linear_function




def test_typical():
    test_func = "5x + 2"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 5
    assert lin_function.calculate_zeros() == -0.4
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_zero_multiply_with_positiv_end():
    test_func = "+ 0 * x + 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() == True
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_zero_multiply_with_negativ_end():
    test_func = "+ 0 * x - 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() == True
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "konstant"
    

def test_one_multiply_with_positive_end():
    test_func = "+ 1 * x + 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 1
    assert lin_function.calculate_zeros() == -1
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_one_negative_multiply_with_negative_end():
    test_func = "- 1 * x - 1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == -1
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "fallend"


def test_one_negative_multiply_with_0_end():
    test_func = "- 1 * x - 0"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == True
    assert lin_function.calculate_monotonicity() == "fallend"


def test_only_x():
    test_func = "x"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == True
    assert lin_function.calculate_monotonicity() == "steigend"


def test_only_negative_x():
    test_func = "- x"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == -1
    assert lin_function.calculate_zeros() == 0
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == True
    assert lin_function.calculate_monotonicity() == "fallend"


def test_only_one():
    test_func = "1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() == True
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_decimal_num_with_different_signs():
    test_func = "0,5 * x + 1.0"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 0.5
    assert lin_function.calculate_zeros() == -2
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "steigend"


def test_only_decimal_num():
    test_func = "0,1"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == "Keine Ableitung möglich."
    assert lin_function.calculate_zeros() == "Keine Nullstelle vorhanden."
    assert lin_function.calculate_symmetry_x() == True
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "konstant"


def test_high_value():
    test_func = "100x + 500"
    lin_function = linear_function.Linear_Func(test_func)
    assert lin_function.calculate_derivative() == 100
    assert lin_function.calculate_zeros() == -5
    assert lin_function.calculate_symmetry_x() == False
    assert lin_function.calculate_point_symmetry_origin() == False
    assert lin_function.calculate_monotonicity() == "steigend"

