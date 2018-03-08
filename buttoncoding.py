def exeval(expression):
    """ The exeval function takes an input of a string with no spaces, and returns a float of the given expression
    """   
    if len(expression) <= 3: #Assuming no spaces (" ") between each value given in the expression
        if expression[0] == "+":
            return float(expression[1]) + float(expression[2])
        elif expression[0] == "-":
            return float(expression[1]) - float(expression[2])
    else:
        if expression[0] == "+":
            return float(expression[1]) + exeval(expression[2:])
        elif expression[0] == "-":
            return float(expression[1]) - exeval(expression[2:])