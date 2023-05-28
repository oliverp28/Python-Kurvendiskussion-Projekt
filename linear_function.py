from curve_discussion_output import Curve_Discussion_Output

class Linear_Func:
    """
        Eine Durchführung einer Kurvendisskussion einer linearen Funktion.
    """

    def __init__(self, function):

        """
            arg: 
                -> Als Eingabe wird ein String mit einer linearen Funktion verarbeitet
                    -> Schema der Funktion: a * x + b
                    --> a bildet im laufe der Funktion a * x ab
                    --> b bildet b ab (alles was nach dem x folgt)

                -> erlaubte Varianten: + o. - ax + o. - b
                    --> Das * zwischen a und x kann weggelassen werden, muss aber nicht
                    --> Abstandsregeln spielen keine Rollen
                -> Nicht erlaubte Eingaben:
                    --> x/a
                    --> a/x
                    --> ax / b
                    --> ax * b

        """

        # Input grob testen auf Richtigkeit
        # Eingaben: '+ 0 * x - 0'
        # x / 0 oder 0 / x
        # 0x
        # 0
        # Try - Except
    
        self.function = self.validate_function(function)

    def validate_function(self, function):
        function = function.replace(" ", "")
        function = function.replace(",", ".")
        function = function.replace("*", "")
        if function.endswith("x"):
            function += "+0"       

        return function
    
    def parse_function(self):  
        function = self.function
        a = ""
        b = ""
        found_x = False
    
        for char in function:
            if char == "x":
                found_x = True
                a += char
                break
            else:
                a += char

        if found_x:
            b = function[len(a):] # Anhand der Länge von a wird, alles um die Stelle 1 nach a in b geladen
        else:
            b = function
            a = ""
         
        a = a.replace("x", "")

        if a == "+" or a == "-":
            a += "1"
        
        
    
        return a, b
    
    def calculate_derivative(self): # a und b in einer Eingabe als Tuple!!
        a, b = self.parse_function()

        if len(a) == 0:
            derivative = "Keine Ableitung von f(x) = " + str(b) + " möglich."
            return derivative
        
        a = eval(a)

        if a == 0:
            derivative = "Keine Ableitung von "+ str(a) + " möglich."
        else:
            derivative = a
        
        return derivative 
            

    #def calculate_symmetry_y(self):
        #a, b = self.parse_function()
        # Fall x = 5 behandeln?

    def calculate_symmetry_x(self):
        a, b = self.parse_function()
        if a == "" or eval(a) == 0 and eval(b) != 0:
            symmetrie_x = True
        else:
            symmetrie_x = False

        return symmetrie_x

    def calculate_point_symmetry_origin(self):
        _, b = self.parse_function()
        b = eval(b)
        if b == 0:
            point_symmetriy_origin = True
        else:
            point_symmetriy_origin = False
        
        return point_symmetriy_origin
    
    def calculate_monotonicity(self):
        a, _ = self.parse_function()
        if a == "":
            monotonicity = "steigend"
        else:
            a = eval(a)
            if a > 0:
                monotonicity = "steigend"
            elif a < 0:
                monotonicity = "fallend"
            else:
                monotonicity = "konstant"

        return monotonicity

        
