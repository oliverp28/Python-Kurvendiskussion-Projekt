"""test cases for the Quadratic_Func class"""
import pytest
from quadratic_function import Quadratic_Func


G1 = "1x**2"  # touchpoint, symmetrical to y-axis
G2 = "1x**2, 2x, -3"  # 2 intersections, not symmetrical
G3 = "1x**2, 5"  # no intersection, symmetrical
G4 = "3x**2, 4x" # not symmetrical
G5 = (1, 2, -3)
G6 = "1x**2, 2x, 3, 4"  # to much entries -> should raise an error
G7 = "-1x**2" # symmetrical

NR1 = 1.0
NR2 = 2.0
NR3 = 5.0

g1_as_func = Quadratic_Func(G1)
g2_as_func = Quadratic_Func(G2)
g3_as_func = Quadratic_Func(G3)
g4_as_func = Quadratic_Func(G4)
g5_as_func = Quadratic_Func(G5)
g7_as_func = Quadratic_Func(G7)


def test_input_validation_to_much_entries():
    """testing instanciation with wrong input"""
    with pytest.raises(RuntimeError):
        Quadratic_Func(G6)


def test_input_validation_one_entry():
    """testing instanciation with only x**2"""
    assert g1_as_func is not None
    assert g1_as_func == Quadratic_Func((1.0, 0.0, 0.0))


def test_input_validation_two_entries():
    """testing instanciation if an object returns with two entries"""
    assert g3_as_func is not None
    assert g4_as_func is not None


def test_input_validation_three_entries():
    """testing instanciation if an object returns with three entries"""
    assert g2_as_func is not None


def test_contains():
    """testing the in-operator"""
    assert NR1 in g1_as_func
    assert NR2 in g2_as_func
    assert NR3 in g3_as_func


def test_contains_not():
    """testing the in operator in negative way"""
    assert NR2 not in g1_as_func
    assert NR3 not in g2_as_func
    assert NR1 not in g4_as_func


def test_pos():
    """testing the plus operator for positiv"""
    assert +g1_as_func == g1_as_func


def test_neg():
    """testing the minus operator for negativ results"""
    assert -g1_as_func == g7_as_func  # g7 is the negative function of g1


def test_add_two_function_same_length():
    """testing plus with two functions with the same length"""
    assert (g2_as_func + g2_as_func) == Quadratic_Func((2.0, 4.0, -6.0))


def test_add_two_function_first_is_shorter():
    """testing plus with two functions, when the first function is shorter"""
    assert (g1_as_func + g2_as_func) == Quadratic_Func((2.0, 2.0, -3.0))


def test_add_two_function_second_is_shorter():
    """testing plus with two functions, when the second functions is shorter"""
    assert (g3_as_func + g1_as_func) == Quadratic_Func((2.0, 0.0, 5.0))


Y_AXIS_SHIFT = 5


def test_add_number():  # known as y-axis-shift in negative in positive direction
    """testing add with a function and a number"""
    assert (g1_as_func + Y_AXIS_SHIFT) == Quadratic_Func((1.0, 0.0, 5.0))
    assert (g2_as_func + Y_AXIS_SHIFT) == Quadratic_Func((1.0, 2.0, 2.0))
    assert (g3_as_func + Y_AXIS_SHIFT) == Quadratic_Func((1.0, 0.0, 10.0))


def test_sub_number():  # known as y-axis-shift in negative direction
    """testing subtraction with a function and a number"""
    assert (g1_as_func - Y_AXIS_SHIFT) == Quadratic_Func((1.0, 0.0, -5.0))
    assert (g2_as_func - Y_AXIS_SHIFT) == Quadratic_Func((1.0, 2.0, -8.0))
    assert (g3_as_func - Y_AXIS_SHIFT) == Quadratic_Func((1.0, 0.0, 0.0))


def test_zeropoints_with_two_intersections():
    """testing the zeropoints function with two zeropoints"""
    assert g2_as_func.zeropoints == (1.0, -3.0)


def test_zeropoints_with_one_intersection():
    """testing the zeropoints function with one zeropoint"""
    assert g1_as_func.zeropoints == 0.0


def test_zeropoints_with_no_intersection():
    """testing the zeropoints function with no zeropoint"""
    assert g3_as_func.zeropoints is None


def test_y_intercept():
    """testing the y_intercept function"""
    assert g2_as_func.y_intercept == -3.0

def test_symmetry():
    """testing if the function is symmetrical to the y axis"""
    assert g1_as_func.symmetry_y_axis is True
    assert g2_as_func.symmetry_y_axis is False
    assert g3_as_func.symmetry_y_axis is True


def test_derivative():
    """testing if the derivative of the quadratic function is right"""
    assert g1_as_func.derivative == (2.0, 0.0)
    assert g2_as_func.derivative == (2.0, 2.0)
    assert g3_as_func.derivative == (2.0, 0.0)
    assert g4_as_func.derivative == (6.0, 4.0)
    assert g5_as_func.derivative == (2.0, 2.0)

def test_extremum():
    """testing if the extremum of the function is right"""
    assert g1_as_func.extremum == (0.0, 0.0)
    assert g2_as_func.extremum == (-1.0, -4.0)
    assert g3_as_func.extremum == (0.0, 5.0)

def test_output():
    """testing the if the output for the output class is fine"""
    assert Quadratic_Func.format_back(g1_as_func) == '1.0x^2'
    assert Quadratic_Func.format_back(g1_as_func.derivative) == '2.0x'
