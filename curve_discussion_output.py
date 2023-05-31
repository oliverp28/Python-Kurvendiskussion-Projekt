class Curve_Discussion_Output:

    def __init__(self, function, function_type="--", derivative=0, zero_lin="--", zeros_quad=("--"), symmetry_x=False, symmetry_origin=False, extremum="--", curvature="--", monotony="--", limes="--"):
        """
            output the results of the curve discussion

            Args:
                function (string) : (Lineare oder Quadratische) Funktion
                function_type (string) : ("lin" oder "quad") Typ der Funktion
                derivative (string) : Ableitung
                zero_lin (string) : Nullstelle
                zeros_quad (tuple) : Nullstellen
                symmetry_x (bool) : Symmetrie zur x-Achse
                symmetry_origin (bool) : Symmetrie zum Ursprung
                extremum  : Extremstellen (Hoch- / Tiefpunkt und Wendepunkt)
                curvature (string) : Krümmungsverhalten
                monotony (string) : Monotonie
                limes (string) : Verhalten gegen Unendlich
        """

        if (len(function) % 2 == 0):
            function = function + " "

        spacing = " " * 20
        max_len = 100

        table_top_bottom = spacing + " " + ("_" * max_len)

        table_split = spacing + " " + ("-" * max_len)

        self.create_header()
        self.create_table_header(spacing, max_len, table_top_bottom, table_split, function)

        if (function_type == "quad"):
            self.fill_table_quad(spacing, table_split, table_top_bottom)
        else:
            self.fill_table_lin(spacing, table_split, table_top_bottom, derivative, zero_lin, symmetry_x, symmetry_origin, monotony)

    def result_end(self, help):
        """
            create the result output for each column

            Args:
                :param help:
        """

        if (len(help) % 2 == 0):
            help += " "

        spacing_help = " " * round(((49 - len(help)) / 2))

        return_val = spacing_help + help + spacing_help + "|"

        return return_val

    def create_header(self):
        """
            print out the header of the output
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

    def create_table_header(self, spacing, max_len, table_top_bottom, table_split,  function):
        """
            print out the header of the table

            Args:
                :param spacing:
                :param max_len:
                :param table_top_bottom:
                :param table_split:
                :param function:
        """

        print(table_top_bottom)

        spacing_help = "FUNKTION:  " + function
        spacing2 = " " * round(((max_len - len(spacing_help)) / 2 ))

        table_gap = spacing + "|" + (" " * max_len) + "|"

        print(table_gap)

        print(spacing + "|" + spacing2 + spacing_help + spacing2 + "|")

        print(table_gap)

        print(table_split)

    def fill_table_lin(self, spacing, table_split, table_top_bottom, derivative, zero_lin, symmetry_x, symmetry_origin, monotony):
        """
            print out the filled table with the results of the Curve Discussion (linear function)

            Args:
                :param spacing:
                :param table_split:
                :param table_top_bottom:
                :param derivative:
                :param zero_lin:
                :param symmetry_x:
                :param symmetry_origin:
                :param monotony:
        """

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|"

        print(gap_splitted)

        result_end = self.result_end(str(derivative))

        print(spacing + "|" + (16 * " ") + "ABLEITUNG / f´(x):" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(zero_lin)

        print(spacing + "|" + (20 * " ") + "NULLSTELLE:" + (19 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if (symmetry_x == True):
            symmetry_x = "JA"
        else:
            symmetry_x = "NEIN"

        result_end = self.result_end(symmetry_x)

        print(spacing + "|" + (14 * " ") + "SYMMETRIE ZUR X-ACHSE ?" + (13 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if (symmetry_origin == True):
            symmetry_origin = "JA"
        else:
            symmetry_origin = "NEIN"

        result_end = self.result_end(symmetry_origin)

        print(spacing + "|" + (13 * " ") + "SYMMETRIE ZUM URSPRUNG ?" + (13 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(monotony)

        print(spacing + "|" + (20 * " ") + "MONOTONIE:" + (20 * " ") + "|" + result_end)
        print(gap_splitted)

        print(table_top_bottom)

    def fill_table_quad(self, spacing, table_split, table_top_bottom):
        """
            print out the filled table with the results of the Curve Discussion (quadratic function)

            Args:
                :param spacing:
                :param table_split:
                :param table_top_bottom:
        """

        result_end = (49 * " ") + "|"

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|"

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