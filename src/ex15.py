"""
Exercise 15
"""


def median(num_list):
    numSort = num_list
    numSort.sort()
    numLen = len(num_list)
    if numLen == 0:
        return None
    elif numLen % 2 == 0:
        index = numLen // 2
        return (numSort[index] + numSort[index - 1]) / 2
    else:
        index = numLen // 2
        return numSort[index]


    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    pass
