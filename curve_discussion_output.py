class Curve_Discussion_Output:

    def __init__(self, function, derivative="--", zeros="--", symmetry="--", extremum="--", curvature="--", monotony="--", limes="--"):
        """
            output the results of the curve discussion
        """

        if (len(function) % 2 == 0):
            function = function + " "

        abstand = " " * 20
        max_len = 100

        table_top_bottom = abstand + " " + ("_" * max_len)

        table_split = abstand + " " + ("-" * max_len)

        self.create_header()
        self.create_table_header(abstand, max_len, table_top_bottom, table_split, function)
        self.fill_table(abstand, table_split, table_top_bottom)

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

    def create_table_header(self, abstand, max_len, table_top_bottom, table_split,  function):

        print(table_top_bottom)

        abstand_help = "FUNKTION:  " + function
        abstand2 = " " * round(((max_len - len(abstand_help)) / 2 ))

        table_gap = abstand + "|" + (" " * max_len) + "|"

        print(table_gap)

        print(abstand + "|" + abstand2 + abstand_help + abstand2 + "|")

        print(table_gap)

        print(table_split)

    def fill_table(self, abstand, table_split, table_top_bottom):

        ende_ergebnis = (49 * " ") + "|"

        gap_splitted = abstand + "|" + (50 * " ") + "|" + (49 * " ") + "|"

        print(gap_splitted)
        print(abstand + "|" + (16 * " ") + "ABLEITUNG / f´(x):" +  (16 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (18 * " ") + "NULLSTELLE(N):" + (18 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (20 * " ") + "SYMMETRIE:" + (20 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (18 * " ") + "EXTREMSTELLEN:" + (18 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (21 * " ") + "KRÜMMUNG:" + (20 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (20 * " ") + "MONOTONIE:" + (20 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_split)

        print(gap_splitted)
        print(abstand + "|" + (18 * " ") + "GRENZVERHALTEN:" + (17 * " ") + "|" + ende_ergebnis)
        print(gap_splitted)

        print(table_top_bottom)
