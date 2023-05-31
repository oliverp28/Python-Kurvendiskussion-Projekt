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
        # Nullstellen ggfs. 

    
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
        replace_a = ""
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

        if "x" in a:
            a = a.replace("x", "")
            replace_a = True
        else:
            replace_a = False

        if a == "+" or a == "-":
            a += "1"
            
        return a, b, replace_a
    
    def calculate_derivative(self): # a und b in einer Eingabe als Tuple!!
        a, _, replace_a = self.parse_function()

        if len(a) == 0 and replace_a == False:
            derivative = "Keine Ableitung möglich."
            return derivative
        
        elif len(a) == 0 and replace_a == True:
            derivative = 1
            return derivative
        

        a = eval(a)

        if a == 0:
            derivative = "Keine Ableitung möglich."
        else:
            derivative = a
        
        return derivative 
            

  #  def calculate_zeros(self):
        a, b, replace_a= self.parse_function()
  
        if a == "" and b != "0" and replace_a == False:
            zero = "Die Funktion hat keine Nullstellen"
            return zero  # Funktion hat keine Nullstellen

        zero = -eval(b) / eval(a)
        return zero

    def calculate_symmetry_x(self):
        a, b, replace_a = self.parse_function()

        if a == "" or eval(a) == 0 and eval(b) != 0:
            symmetrie_x = True
            if a == "" and replace_a == True:
                symmetrie_x = False

        else:
            symmetrie_x = False

        return symmetrie_x
    

    def calculate_point_symmetry_origin(self):
        _, b, _ = self.parse_function()
        b = eval(b)
        if b == 0:
            point_symmetriy_origin = True
        else:
            point_symmetriy_origin = False
        
        return point_symmetriy_origin
    

    def calculate_monotonicity(self):
        a, _, replace_a = self.parse_function()
    
        if a == "": # x wurde abgeschnitten aber der Fall f(x) = x wird hier behandelt
            if replace_a == True:
                monotonicity = "steigend"
            else:
                monotonicity = "konstant"
        else:
            a = eval(a)
            if a > 0:
                monotonicity = "steigend"
            elif a < 0:
                monotonicity = "fallend"
            else:
                monotonicity = "konstant"

        return monotonicity

        
