from quadratic import Quadratic_Func

g1 = "1x**2" # beruehrpunkt
g2 = "1x**2, 2x, -3" # 2 schnittpunkte
g3 = "1x**2, 5" # kein schnittpunkt
g4 = "3x**2, 4x"
g5 = (1, 2, 3)

g1_as_func = Quadratic_Func(g1)
g2_as_func = Quadratic_Func(g2)
g3_as_func = Quadratic_Func(g3)
g4_as_func = Quadratic_Func(g4)
g5_as_func = Quadratic_Func(g5)

def test_asdf():
    assert g5_as_func is not None


def test_input_validation_one_entry():
    assert g1_as_func is not None
    # assert g1_as_func == (1.0, 0.0, 0.0)

def test_input_validation_two_entries():
    assert g3_as_func is not None
    assert g4_as_func is not None

def test_input_validation_three_entries():
    assert g2_as_func is not None


def test_add_two_function_same_length():
    assert (g2_as_func + g2_as_func) == Quadratic_Func((2.0, 4.0, -6.0)) 

def test_add_two_function_first_is_shorter():
    assert (g1_as_func + g2_as_func) == Quadratic_Func((2.0, 2.0, -3.0))

def test_add_two_function_second_is_shorter():
    assert (g3_as_func + g1_as_func) == Quadratic_Func((2.0, 0.0, 5.0))


y_verschiebung = 5
# def test_add_number(): # bekannt auch als y-Achsenverschiebung
#     assert (g1_as_func + y_verschiebung) == ("1", "0", "5")
#     assert (g2_as_func + y_verschiebung) == ("1", "2", "2")
#     assert (g3_as_func + y_verschiebung) == ("1", "0", "10")

# def Nullstelle_berechnen_2_Schnittpunkte():


# def Nullstelle_berechnen_Beruehrpunkt():


# def Nullstelle_berechnen_kein_Schnittpunkt():
