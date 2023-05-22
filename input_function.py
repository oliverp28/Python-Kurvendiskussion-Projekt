from linear_function import Linear_Function
from quadratic_function import Quadratic_Function

class Input_Function:

    def __init__(self):
        """
            get and validate input function
        """
        self.get_function()

    def get_function(self):

        function = input("Gib deine Funktion ein: ")
        print("Du hast folgende Funktion eingegeben:", function)