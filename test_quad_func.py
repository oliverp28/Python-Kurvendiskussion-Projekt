from quadratic import Quadratic_Func
import pytest


# TODO: pos neg

g1 = "1x**2" # touchpoint
g2 = "1x**2, 2x, -3" # 2 intersections
g3 = "1x**2, 5" # no intersection
g4 = "3x**2, 4x"
g5 = (1, 2, -3)
g6 = "1x**2, 2x, 3, 4" # to much entries -> should raise an error
g7 = "-1x**2"

nr1 = 1.0
nr2 = 2.0
nr3 = 5.0

g1_as_func = Quadratic_Func(g1)
g2_as_func = Quadratic_Func(g2)
g3_as_func = Quadratic_Func(g3)
g4_as_func = Quadratic_Func(g4)
g5_as_func = Quadratic_Func(g5)
g7_as_func = Quadratic_Func(g7)

def test_input_validation_to_much_entries():
    with pytest.raises(RuntimeError): 
        Quadratic_Func(g6)


def test_input_validation_one_entry():
    assert g1_as_func is not None
    assert g1_as_func == Quadratic_Func((1.0, 0.0, 0.0))

def test_input_validation_two_entries():
    assert g3_as_func is not None
    assert g4_as_func is not None

def test_input_validation_three_entries():
    assert g2_as_func is not None


def test_contains():
    assert nr1 in g1_as_func 
    assert nr2 in g2_as_func 
    assert nr3 in g3_as_func

def test_contains_not():
    assert nr2 not in g1_as_func
    assert nr3 not in g2_as_func
    assert nr1 not in g4_as_func

def test_pos():
    assert +g1_as_func == g1_as_func

def test_neg():
    assert -g1_as_func == g7_as_func # g7 is the negative function of g1

def test_add_two_function_same_length():
    assert (g2_as_func + g2_as_func) == Quadratic_Func((2.0, 4.0, -6.0)) 

def test_add_two_function_first_is_shorter():
    assert (g1_as_func + g2_as_func) == Quadratic_Func((2.0, 2.0, -3.0))

def test_add_two_function_second_is_shorter():
    assert (g3_as_func + g1_as_func) == Quadratic_Func((2.0, 0.0, 5.0))


def test_sub_two_function_same_length():
    assert (g2_as_func - g2_as_func) == Quadratic_Func((0.0, 0.0, 0.0)) 

def test_sub_two_function_first_is_shorter():
    assert (g1_as_func - g2_as_func) == Quadratic_Func((0.0, -2.0, 3.0))

def test_sub_two_function_second_is_shorter():
    assert (g3_as_func - g1_as_func) == Quadratic_Func((0.0, 0.0, 5.0))


y_axis_shift = 5
def test_add_number(): # known as y-axis-shift in negative in positive direction
    assert (g1_as_func + y_axis_shift) == Quadratic_Func((1.0, 0.0, 5.0))
    assert (g2_as_func + y_axis_shift) == Quadratic_Func((1.0, 2.0, 2.0))
    assert (g3_as_func + y_axis_shift) == Quadratic_Func((1.0, 0.0, 10.0))

def test_sub_number(): # known as y-axis-shift in negative direction
    assert (g1_as_func - y_axis_shift) == Quadratic_Func((1.0, 0.0, -5.0))
    assert (g2_as_func - y_axis_shift) == Quadratic_Func((1.0, 2.0, -8.0))
    assert (g3_as_func - y_axis_shift) == Quadratic_Func((1.0, 0.0, 0.0))


def test_nullstelle_berechnen_2_Schnittpunkte():
    assert g2_as_func.zeropoints == (1.0, -3.0)

def test_nullstelle_berechnen_Beruehrpunkt():
    assert g1_as_func.zeropoints == 0.0

def test_nullstelle_berechnen_kein_Schnittpunkt():
    assert g3_as_func.zeropoints == None
