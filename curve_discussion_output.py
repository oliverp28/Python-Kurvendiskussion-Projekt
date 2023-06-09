class Curve_Discussion_Output: # Class for outputting the curve analysis
    """This module contains a class for outputting a curve analysis using precalculated values."""
    def __init__(self,
                 function,
                 function_type="--",
                 derivative=0,
                 zero_lin="--",
                 zeros_quad=("--"),
                 symmetry_x=False,
                 symmetry_y=False,
                 symmetry_origin=False,
                 extremum="--",
                 monotonicity="--"):
        """
            Outputs the results of the curve analysis.

            Args:
                function (string): (Linear or quadratic) function
                function_type (string): ("lin" or "quad") type of function
                derivative (string): derivative
                zero_lin (string): zero of the linear function
                zeros_quad (tuple): zeros of the quadratic function
                symmetry_x (bool): symmetry with respect to the x-axis
                symmetry_y (bool): symmetry with respect to the y-axis
                symmetry_origin (bool): symmetry with respect to the origin
                extremum (): extrema (maximum/minimum points and inflection point)
                curvature (string): curvature behavior
                monotonicity (string): monotonicity
                limes (string): behavior at infinity
        """

        spacing_end = " " * 9 + "║"

        if len(function) % 2 == 0:
            function = function + " "

        spacing =  " " * 12 + "║" + " " * 8
        max_len = 100

        table_top_bottom = spacing + " " + ("_" * max_len) + spacing_end # Separator line for table header and footer

        table_split = spacing + " " + ("-" * max_len) + spacing_end # Separator line for table columns

        self.create_header() # Create and output the header of the output
        self.create_table_header(spacing, max_len, table_top_bottom, table_split, function) # Create and output the table header

        if function_type == "quad":
            self.fill_table_quad(spacing, table_split, table_top_bottom, derivative, zeros_quad, symmetry_y, extremum) # Create a table for a quadratic function.
        else:
            self.fill_table_lin(spacing, table_split, table_top_bottom, derivative, zero_lin, symmetry_x, symmetry_origin, monotonicity) # Create a table for a linear function

        self.create_footer() # Create footer of table

    def result_end(self,
                   input_var):
        """
            Generates the output/result for each column.
                -> Prepares input for output.

            Args:
                input_var: Input variable
        """

        spacing_end = " " * 8 + "║"

        if len(input_var) % 2 == 0:
            input_var += " "

        spacing_help = " " * round(((49 - len(input_var)) / 2))

        return_val = spacing_help + input_var + spacing_help + "|" + spacing_end

        return return_val

    def create_header(self):
        """To output the header of the output."""
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
            Outputs the table header.

            Args:
                spacing: Spacing for indentation
                max_len: Maximum width of the table
                table_top_bottom: Separator line for table header and footer
                table_split: Separator line for table columns
                function: Function type
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
            Outputs the filled table with the results of the curve analysis (linear function).

            Args:
                spacing: Spacing for indentation
                table_split: Separator line for table columns
                table_top_bottom: Separator line for table header and footer
                derivative: Derivative
                zero_lin: Zero of the linear function
                symmetry_x: Symmetry with respect to the x-axis
                symmetry_origin: Symmetry with respect to the origin
                monotonicity: Monotonicity
        """

        spacing_end = " " * 8 + "║"

        gap_splitted = spacing + "|" + (50 * " ") + "|" + (49 * " ") + "|" + spacing_end # Separator line for table columns with a vertical bar in the middle

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

        print(spacing + "|" + (18 * " ") + "NULLSTELLE (X):" + (17 * " ") + "|" + result_end)

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
                        table_top_bottom,
                        derivative,
                        zeros_quad,
                        symmetry_y,
                        extremum):
        """
            Outputs the filled table with the results of the curve analysis (quadratic function).

            Args:
                spacing: Spacing for indentation
                table_split: Separator line for table columns
                table_top_bottom: Separator line for table header and footer
                derivative: Derivative
                zeros_quad: Zeros of the quadratic function
                symmetry_y: Symmetry with respect to the y-axis
                extremum: Extrema
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

        result_end = self.result_end(derivative)

        print(spacing + "|" + (16 * " ") + "ABLEITUNG / f´(x):" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if zeros_quad is None:
            zeros_quad = "Keine Nullstellen vorhanden"

        result_end = self.result_end(str(zeros_quad))

        print(spacing + "|" + (16 * " ") + "NULLSTELLE(N) (X):" + (16 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        if symmetry_y is True:
            symmetry_y = "JA"
        else:
            symmetry_y = "NEIN"

        result_end = self.result_end(str(symmetry_y))

        print(spacing + "|" + (14 * " ") + "SYMMETRIE ZUR Y-ACHSE ?" + (13 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_split)

        print(gap_splitted)

        result_end = self.result_end(str(extremum))

        print(spacing + "|" + (15 * " ") + "EXTREMSTELLE (X, Y):" + (15 * " ") + "|" + result_end)

        print(gap_splitted)

        print(table_top_bottom)

        print(spacing + 110 * " " + "║")

    def create_footer(self):
        """Outputs the footer of the table."""
        print(
            """
            ║██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████║
            ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            """
        )

        print((47 * " ") + "╔═ © created by Oliver P., Stefan, Rami and David ═╗")

        print((47 * " ") + "╚══════════════════════════════════════════════════╝")
