from linear_function import LinearFunction
from quadratic_function import QuadraticFunction

class InputFunction:

    def __init__(self):
        """
            get and validate input function
        """
        self.get_function()

    def get_function(self):

        function = input("Gib deine Funktion ein: ")
        print("Du hast folgende Funktion eingegeben:", function)