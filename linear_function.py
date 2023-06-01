from curve_discussion_output import Curve_Discussion_Output


class Linear_Func:
    """
    Eine Durchführung einer Kurvendisskussion einer linearen Funktion
    Bestandteile:
                - Ableitung
                - Nullstelle
                - Symmetrie zur x-Achse
                - Symmetrie zum Ursprung
                - Monotonie
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

        self.function = self.validate_function(
            function
        )  # function, als Verwendung in Form einer Klassenvariable

        self.calculate_derivative()  # Aufruf der Funktionen
        self.calculate_symmetry_x()
        self.calculate_point_symmetry_origin()
        self.calculate_monotonicity()

    def validate_function(self, function):
        """
        Validierung der eingegebenen Funktion
        Args:
            function (str): Der String mit der linearen Funktion
        Returns:
            str: Die validierte Funktion
        """
        function = function.replace(" ", "")  # entfernen von Abständen
        function = function.replace(",", ".")  # Standardisierung von , in .
        function = function.replace(
            "*", ""
        )  # entfernen von * für Falle wie: 5*x zu 5x für bessers rechnen
        if function.endswith(
            "x"
        ):  # hinzufügen von + 0 bei Funktionen wie 5x, für eine Analyse von b
            function += "+0"

        return function

    def parse_function(self):
        """
        Analysieren der Funktion auf die einzelnen Bestandteile

        Args:
            function (str): Der String mit der linearen Funktion

        Returns:
            a: Funktionsteil bis einschließlich x
            b: Funktionsteil ab x bis zum Ende
            replace_a: Kontroll-Variable zur Analyse von seltenen Fällen
        """
        function = self.function
        a = ""  # Instanziierung von Variablen
        b = ""
        replace_x = ""  # Kontrollvariable für Funktionen wie f(x) = x
        found_x = False

        for char in function:  # Untersuche ob x enhalten ist
            if char == "x":
                found_x = True  # Ist x enhalten wird der Teil bis einschließlich x in a geladen
                a += char
                break
            else:
                a += char

        if found_x:
            b = function[
                len(a) :
            ]  # Anhand der Länge von a wird, alles um die Stelle 1 nach a in b geladen
        else:
            b = function  # ist kein x vorhanden wird alles in b geladen
            a = ""

        if (
            "x" in a
        ):  # x wird in a entfernt, damit mathematische Berechnungen möglich sind
            a = a.replace("x", "")
            replace_x = True  # diese Kontrollvariable wird bei Fallunterscheidungen miteinbezogen
        else:
            replace_x = False

        if (
            a == "+" or a == "-"
        ):  # ist ein x und wird für den Fall +x oder -x eine 1 für x eingesetzt
            a += "1"

        return a, b, replace_x

    def calculate_derivative(self):
        """
        Berechnung der Ableitung.

        Args:
            Verwendung der Bestandteile der Funktion als String in a, b und replace_a

        Returns:
            derivative: int; float; string (Datentyp abhängig von der linearen Funktion)
        """
        a, _, replace_x = self.parse_function()

        if (
            len(a) == 0 and replace_x is False
        ):  # Test für den Fall dass keine Steigung vorhanden ist wie f(x) = 5
            derivative = "Keine Ableitung möglich."
            return derivative

        elif (
            len(a) == 0 and replace_x is True
        ):  # Test für den Fall dass die Funktion f(x) = x lautet
            derivative = 1
            return derivative

        a = eval(a)  # Umrechnung von +0 oder -0 in 0

        if a == 0:  # Test für f(x) = 0x + 2
            derivative = "Keine Ableitung möglich."
        else:
            derivative = a

        return derivative

    def calculate_zeros(self):
        """
        Berechnung der Nullstellen.

        Args:
            Verwendung der Bestandteile der Funktion als String in a, b und replace_a

        Returns:
            zero: int; float; string (Datentyp abhängig von der linearen Funktion)
        """
        a, b, replace_x = self.parse_function()

        if len(a) == 0:  # Test für f(x) = x
            if replace_x is True and eval(b) == 0:
                zero = 0
                return zero

            elif replace_x is True and eval(b) != 0:  # Test für f(x) = x + 1
                zero = -eval(b) / 1  # Berechnung der Nullstelle mit a = 1
                return zero

            elif replace_x is False:  # Test für den Fall von keinem a
                zero = "Keine Nullstelle vorhanden."
                return zero

        if eval(a) == 0:  # Test für den Fall f(x) = -0x + 5
            zero = "Keine Nullstelle vorhanden."
            return zero

        if replace_x is True and b == "0":  # Test für den Fall f(x) = 5x
            zero = 0
            return zero

        if len(a) >= 1:  # Test für den Fall f(x) = 5x + 10
            zero = -eval(b) / eval(a)
            return zero

    def calculate_symmetry_x(self):

        """
        Feststellung der Symmetrie zur X-Achse

        Args:
            Verwendung der Bestandteile der Funktion als String in a, b und replace_a

        Returns:
            symmetrie_x: bool
        """

        a, b, replace_x = self.parse_function()

        if a == "" or eval(a) == 0 and eval(b) != 0:  # Test für a = 0 und b != 0
            symmetry_x = True
            if a == "" and replace_x is True:  # Test für a != 0x
                symmetry_x = False

        else:  # Test sobald a != 0x ist
            symmetry_x = False

        return symmetry_x

    def calculate_point_symmetry_origin(self):

        """
        Feststellung der Symmetrie zum Ursprung

        Args:
            Verwendung der Bestandteile der Funktion als String in b

        Returns:
            point_symmetrie_origin: bool
        """

        _, b, _ = self.parse_function()
        b = eval(b)
        if b == 0:  # Test ob b 0 entspricht
            point_symmetry_origin = True
        else:
            point_symmetry_origin = (
                False  # gilt für alle Fälle wenn b != 0 wie f(x) = 5x + 2
            )

        return point_symmetry_origin

    def calculate_monotonicity(self):

        """
            Feststellung der Monotonie

            Args:
            Verwendung der Bestandteile der Funktion als String in b

        Returns:
            monotonicity: string
        """
        a, _, replace_x = self.parse_function()

        if a == "":  # x wurde abgeschnitten aber der Fall f(x) = x wird hier behandelt
            if replace_x is True:
                monotonicity = "steigend"
            else:
                monotonicity = (
                    "konstant"  # Test des Falls dass keine Steigung in a vorhanden ist
                )
        else:
            a = eval(a)  # Test ob a a = 0 oder größer oder kleiner ist
            if a > 0:
                monotonicity = "steigend"
            elif a < 0:
                monotonicity = "fallend"
            else:
                monotonicity = "konstant"

        return monotonicity
