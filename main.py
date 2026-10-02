# The goal of this short coding project is build a simple Python calculator
# We will use a "Calculator" class without using the Python dataclass to build the class
# The calculator class should support operations such as multiplication, division, addition, and subtraction
# When performing an operation, the input can either be in the form val1, operator, and val2. Or just operator, val2
# In the latter case, the object will use the most recent calculated value stored in the history
# You can also get the Calculator's history of previous operations

import re

def add_vals(a, b): return a + b

def sub_vals(a, b): return a - b

def mul_vals(a, b): return a * b

def div_vals(a, b): return a / b

operator_dict = {"+": add_vals, "-": sub_vals, "*": mul_vals, "/": div_vals,}

class Calculator:
    def __init__(self):
        self.history = [0]

    def __str__(self):
        return f"Calculator: {self.history}"

    def operate(self, a, operator, b):
        try:
            result = operator_dict[operator](a, b)
            self.history.append(result)
            return result
        except ZeroDivisionError:
            return "Divide by zero"
        except KeyError:
            return "Please pass in a valid operator"



if __name__ == '__main__':
    TI82 = Calculator()

    while True:
        user_input = input("Input: ")
        if user_input == "Exit":
            break
        split_user_input = re.findall(r'\d+|\S', user_input)

        match split_user_input:
            case [val1, operator, val2] if val1.isdigit() and val2.isdigit():
                print(TI82.operate(int(val1), operator, int(val2)))
            case [operator, val2] if val2.isdigit() and not operator.isdigit():
                print(TI82.operate(TI82.history[-1], operator, int(val2)))
            case _:
                print("Invalid format")

    print(TI82)

# INVALID INPUT CASES
#
#++3
#2++3
#12321 + 3 + 1321321
#123213++123 + 123231

# VALID INPUT CASES
#2+3
#2 + 3
#2 +   3
#+ 3
# +   3

# It doesn't matter how many spaces an input has, it can come in either of two forms
# val1operatorval2
# operatorval2
# val1+ doesn't work either
# Just check for these, get the string, strip the spaces, break the string up before and after an operator
# In regex terms, 1,2 numbers,
# you don't want to hardcode the operators here
# I need a combination of string splitting and matching
# I need to break the string around an operator, a symbol.