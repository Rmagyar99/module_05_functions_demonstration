"""
Description: Module 05 demonstration: Functions
Author: Reiley Magyar
Date: October 23, 2023
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet() ->None:
    """
    Prints a greeting message to the console.
    Returns :
        None
    """
    print("Hello World!")



def greet_name_age(name: str, age: int) ->None:
    """
    Prints a greeting which includes the values of the name 
    and age parameters (inputs).
    Args:
        name (str): The name of the person being greeted.
        age (int): The age of the person being greeted.
    Returns: 
        None
    """
    print(f"Hello {name}, you are {age} years old.")



def math_operation(operand_1: int, operand_2: int, operator: str) -> float:
    """
    Returns the result of the specified math operation based on the
    values of the two operands.
    Args:
        operand_1 (int): Represents the left-side of the operation.
        operand_2 (int): Represents the right-side of the operation.
        operator (str): The operation to perform.
    Return:
        float: The result of the operation.
    Raises:
        ValueError: When the operator is not a + or -
            "Invalid operation: Must be a + or -."
    """
    if operator == "+":
        result = operand_1 + operand_2
    elif operator == "-":
        result = operand_1 - operand_2
    else:
        raise  ValueError("Invalid operation: Must be + or -.")

    return float(result)



try:
    result = math_operation(1, 3, "+")  # 4.0
    print(result)
except ValueError as e:
    print(e)


try:
    print(math_operation(6, 10, "-"))  # -4.0
except ValueError as e:
    print(e)

try:
    print(math_operation(5, 5, "*"))  # 25.0
except ValueError as e:
    print(e)

print("End of file.")

print(math_operation.__doc__)
print(print.__doc__)