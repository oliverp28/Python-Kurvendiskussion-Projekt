"""
    Dieses Modul enthält eine Klasse zur Ausgabe einer Kurvendiskussion, mithilfe der zuvor berechneten Werte.
"""
class Curve_Discussion_Output: # Klasse für die Ausgabe der Kurvendiskussion
    def __init__(self,
                 function,
                 function_type="--",
                 derivative=0,
                 zero_lin="--",
                 zeros_quad=("--"),
                 symmetry_x=False,
                 symmetry_origin=False,
                 extremum="--",
                 curvature="--",
                 monotonicity="--",
                 limes="--"):

        """
            Gibt die Ergebnisse der Kurvendiskussion aus.

            Args:
                function (string) : (Lineare oder Quadratische) Funktion
                function_type (string) : ("lin" oder "quad") Typ der Funktion
                derivative (string) : Ableitung
                zero_lin (string) : Nullstelle
                zeros_quad (tuple) : Nullstellen
                symmetry_x (bool) : Symmetrie zur x-Achse
                symmetry_origin (bool) : Symmetrie zum Ursprung
                extremum (): Extremstellen (Hoch- / Tiefpunkt und Wendepunkt)
                curvature (string) : Krümmungsverhalten
                monotonicity (string) : Monotonie
                limes (string) : Verhalten gegen Unendlich
        """

        spacing_end = " " * 9 + "║"

        if len(function) % 2 == 0:
            function = function + " "

        spacing =  " " * 12 + "║" + " " * 8
        max_len = 100

        table_top_bottom = spacing + " " + ("_" * max_len) + spacing_end # Trennlinie für Tabellenkopf und -ende

        table_split = spacing + " " + ("-" * max_len) + spacing_end # Trennlinie für Tabellenspalten

        self.create_header() # Header der Ausgabe erstellen und ausgeben
        self.create_table_header(spacing, max_len, table_top_bottom, table_split, function) # Tabellenkopf erstellen und ausgeben

        if function_type == "quad":
            self.fill_table_quad(spacing, table_split, table_top_bottom) # Tabelle für quadratische Funktion erstellen
        else:
            self.fill_table_lin(spacing, table_split, table_top_bottom, derivative, zero_lin, symmetry_x, symmetry_origin, monotonicity) # Tabelle für lineare Funktion erstellen

        self.create_bottom()

    def result_end(self,
                   input_var):

        """
            Erzeugt die Ausgabe/ das Ergebnis für jede Spalte.
                -> Input wird aufbereitet für die Ausgabe

            Args:
                input_var: Inputvariable
        """

        spacing_end = " " * 8 + "║"

        if len(input_var) % 2 == 0:
            input_var += " "

        spacing_help = " " * round(((49 - len(input_var)) / 2))

        return_val = spacing_help + input_var + spacing_help + "|" + spacing_end

        return return_val

    def create_header(self):

        """
            Gibt den Header der Ausgabe aus.
        """
        print(
            """
             ██████╗██╗   ██╗██████╗ ██╗   ██╗███████╗    ██████╗ ██╗███████╗ ██████╗██╗   ██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
            ██╔════╝██║   ██║██╔══██╗██║   ██║██╔════╝    ██╔══██╗██║██╔════╝██╔════╝██║   ██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
            ██║     ██║   ██║██████╔╝██║   ██║█████╗      ██║  ██║██║███████╗██║     ██║   ██║███████╗███████╗██║██║   ██║██╔██╗ ██║
            ██║     ██║   ██║██╔══██╗╚██╗ ██╔╝██╔══╝      ██║  ██║██║╚════██║██║     ██║   ██║╚════██║╚════██║██║██║   ██║██║╚██╗██║
            ╚██████╗╚██████╔╝██║  ██║ ╚████╔╝ ███████╗    ██████╔╝██║███████║╚██████╗╚██████╔╝███████║███████║██║╚██████╔╝██║ ╚████║
             ╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
            """
        )

    def create_table_header(self,
                            spacing,
                            max_len,
                            table_top_bottom,
                            table_split,
                            function):

        """
            Gibt den Tabellenkopf aus.

            Args:
                spacing: Leerzeichen für Einrückungen
                max_len: Maximale Breite der Tabelle
                table_top_bottom: Trennlinie für Tabellenkopf und -ende
                table_split: Trennlinie für Tabellenspalten
                function: Funktionstyp
        """

        spacing_end = " " * 8 + "║"

        print(table_top_bottom)

        spacing_help = "FUNKTION:  " + function
        spacing2 = " " * round(((max_len - len(spacing_help)) / 2 ))

        table_gap = spacing + "|" + (" " * max_len) + "|" + spacing_end

        print(table_gap)

        print(spacing + "|" + spacing2 + spacing_help + spacing2 + "|" + spacing_end)

        print(table_gap)

        print(table_split)

    def fill_table_lin(self,
                       spacing,
                       table_split,
                       table_top_bottom,
                       derivative,
                       zero_lin,
                       symmetry_x,
                       symmetry_origin,
                       monotonicity):

        """
            Gibt die gefüllte Tabelle mit den Ergebnissen der Kurvendiskussion (lineare Funktion) aus.

            Args:
                spacing: Leerzeichen für Einrückungen
                table_split: Trennlinie für Tabellenspalten
                table_top_bottom: Trennlinie für Tabellenkopf und -ende
                derivative: Ableitung
                zero_lin: Nullstelle
                symmetry_x: Symmetrie zur x-Achse
                symmetry_origin: Symmetrie zum Ursprung
                monotonicity: Monotonie
        """

        spacing_end = " " * 8 + "║"

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|" + spacing_end # Trennlinie für Tabellenspalten mit einem Trennstrich in der Mitte

        print(gap_splitted)

        result_end = self.result_end("lineare Funktion")

        print(spacing + "|" + (17 * " ") + "ART DER FUNKTION:" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(str(derivative))

        print(spacing + "|" + (16 * " ") + "ABLEITUNG / f´(x):" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(str(zero_lin))

        print(spacing + "|" + (20 * " ") + "NULLSTELLE:" + (19 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if symmetry_x is True:
            symmetry_x = "JA"
        else:
            symmetry_x = "NEIN"

        result_end = self.result_end(symmetry_x)

        print(spacing+"|" + (14 * " ") + "SYMMETRIE ZUR X-ACHSE ?" + (13 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if symmetry_origin is True:
            symmetry_origin = "JA"
        else:
            symmetry_origin = "NEIN"

        result_end = self.result_end(symmetry_origin)

        print(spacing+"|" + (13 * " ") + "SYMMETRIE ZUM URSPRUNG ?" + (13 * " ") + "|"+result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(monotonicity)

        print(spacing + "|" + (20 * " ") + "MONOTONIE:" + (20 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_top_bottom)

        print(spacing + 110 * " " + "║")

    def fill_table_quad(self,
                        spacing,
                        table_split,
                        table_top_bottom):

        """
            Gibt die gefüllte Tabelle mit den Ergebnissen der Kurvendiskussion (quadratische Funktion) aus.

            Args:
                spacing: Leerzeichen für Einrückungen
                table_split: Trennlinie für Tabellenspalten
                table_top_bottom: Trennlinie für Tabellenkopf und -ende
        """

        spacing_end = " " * 8 + "║"

        result_end = (49 * " ") + "|"

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|" + spacing_end

        print(gap_splitted)

        result_end = self.result_end("quadratische Funktion")

        print(spacing + "|" + (17 * " ") + "ART DER FUNKTION:" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (16 * " ") + "ABLEITUNG / f´(x):" + (16 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (18 * " ") + "NULLSTELLE(N):" + (18 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (20 * " ") + "SYMMETRIE:" + (20 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (18 * " ") + "EXTREMSTELLEN:" + (18 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (21 * " ") + "KRÜMMUNG:" + (20 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (20 * " ") + "MONOTONIE:" + (20 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(spacing + "|" + (18 * " ") + "GRENZVERHALTEN:" + (17 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_top_bottom)

        print(spacing + 110 * " " + "║")

    def create_bottom(self):
        print(
            """
            ║██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████║
            ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            """
        )
