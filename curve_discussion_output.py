class Curve_Discussion_Output:

    def __init__(self, function, derivative="--", zeros="--", symmetry="--", extremum="--", curvature="--", monotony="--", limes="--"):
        """
            output the results of the curve discussion

            Args:
                function (string) : (Lineare oder Quadratische) Funktion
                derivative (string) : Ableitung
                zeros (list) : Nullstellen
                symmetry (string) : Symmetrie
                extremum (list) : Extremstellen (Hoch- / Tiefpunkt und Wendepunkt)
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
        self.fill_table(spacing, table_split, table_top_bottom)

    def create_header(self):
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

        print(table_top_bottom)

        spacing_help = "FUNKTION:  " + function
        spacing2 = " " * round(((max_len - len(spacing_help)) / 2 ))

        table_gap = spacing + "|" + (" " * max_len) + "|"

        print(table_gap)

        print(spacing + "|" + spacing2 + spacing_help + spacing2 + "|")

        print(table_gap)

        print(table_split)

    def fill_table(self, spacing, table_split, table_top_bottom):

        result_end = (49 * " ") + "|"

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|"

        print(gap_splitted)
        print(spacing + "|" + (16 * " ") + "ABLEITUNG / f´(x):" +  (16 * " ") + "|" + result_end)
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