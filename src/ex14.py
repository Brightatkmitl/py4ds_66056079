"""
Exercise 14
"""


def average(num_list: list) -> float:
    calAvg = 0
    for i in num_list:
        calAvg = calAvg +i
    return calAvg / len(num_list)
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    pass
