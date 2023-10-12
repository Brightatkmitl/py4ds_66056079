"""
Exercise 13
"""


def calc_sum(num_list):
    calSum = 0
    for i in num_list:
        calSum = calSum + i

    return calSum
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    pass


def calc_prod(num_list):
    calMul = 1
    for i in num_list:
        calMul = calMul * i
    return calMul

    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    pass
