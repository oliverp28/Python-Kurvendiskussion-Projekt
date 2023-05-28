from curve_discussion_output import Curve_Discussion_Output

class Quadratic_Func:
    
    def __init__(self, input, *, _format = True):
        """Instanciate the input from the validation class
         
        Args: 
            input (sequenz in special form): quadratic function
        """
        entry_list = input

        if  isinstance(entry_list, (tuple, list)):
            if len(entry_list) == 3:
                _format = False
                for asdf_entry in entry_list:
                    if not isinstance(asdf_entry, (int, float)):
                        _format = True
        
        if _format:

            if isinstance(input, str):
                entry_list = input.split(", ")
            if not isinstance (entry_list, list):
                entry_list = list(entry_list)

        
            for index, entry in enumerate(entry_list): # removing the x's to work with the numbers

                if index == 0:
                    if isinstance(entry, str):
                        entry_list[index] = entry.replace("x**2", "")
                    if entry == "":
                        entry_list[index] = "1"

                elif index == 1:
                    if isinstance(entry, str):
                        if "x" in entry:
                            entry_list[index] = entry.replace("x", "")
                            if entry == "":
                                entry_list[index] = "1"
                            continue
                        if len(entry_list) == 2:
                            entry_list.insert(index, "0")

                elif index == 2:
                    entry_list[index] = entry

            if len(entry_list) == 2:
                entry_list.append(0.0)        

            try: # testing if every entry is a number
                for i, func_entry in enumerate(entry_list):
                    entry_list[i] = float(func_entry)
            except ValueError:
                raise RuntimeError("faulty input")
        self._func = tuple(entry_list)
        print(self._func)


    def __repr__(self): # TODO
        return "Quadratic_func(" + repr(self._func) + ")"
    
    def __iter__(self):
        return iter(self._func)


    def __add__(self, other):
        if isinstance(other, Quadratic_Func): # TODO replace Quadratic_Func with general func
            temp = [x + y for x, y in zip (self._func, other._func)]
            return Quadratic_Func(temp, _format = False)

