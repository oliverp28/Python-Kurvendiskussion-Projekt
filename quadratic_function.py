from curve_discussion_output import CurveDiscussionOutput

class Quadratic_Func:
    
    def __init__(self, input):
        """Instanciate the input from the validation class
        
        Args: 
            input (sequenz in special form): quadratic function
        """
        entry_list = [input.split(", ")]
            
        while(len(entry_list) < 3): # length of a quadratic function
            entry_list.append("0")

        for index in range(3): # removing the x's to work with the numbers
            if "x^2" in entry_list[index] and index == 0:
                entry_list[index] = entry_list[index].replace("x**2", "")
                if entry_list[index] == "":
                    entry_list = "1"

            elif "x" in entry_list[index] and index == 1:
                entry_list[index] = entry_list[index].replace("x", "")
                if entry_list[index] == "":
                    entry_list = "1"

            elif "x" not in entry_list[index] and index < 2:
                entry_list[index] = "0"

            else:
                entry_list[index] = entry_list[index]


        structured_func = tuple(entry_list) 
        try: # testing if every entry is a number
            for func_entry in structured_func:
                float(func_entry)
        except ValueError:
            raise RuntimeError("faulty input")
            
        self._func = structured_func

    # TODO
    #def __repr__(self):
    #    format = ("x^2", "x", "")
    #    output = zip(self, format)
        
    #   return "Quadratic_func(" + repr(output) + ")"
    
    # def __iter__(self):
    #     return iter(self)


    # def __add__(self, other):
    #     if isinstance(object, valid.Validated_Func):
    #         if(len(other) == 2):
    #             return
            
