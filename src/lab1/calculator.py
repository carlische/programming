def addition(first_arg, second_arg):
    """
    Returns the sum of two numbers
    """
    return first_arg + second_arg


def subtraction(first_arg, second_arg):
    """
    Returns the difference of two numbers
    """
    return first_arg - second_arg


def multiplication(first_arg, second_arg):
    """
    Returns the product of two numbers
    """
    return first_arg * second_arg


def division(first_arg, second_arg):
    """
    Returns the quotient of two numbers divided
    """
    if second_arg != 0:
        return first_arg / second_arg
    return "Error: division by zero"

if __name__ == '__main__':
    print(eval(input()))