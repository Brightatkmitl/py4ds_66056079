"""
Execise 12
"""


def get_smallest(num_list):
    if len(num_list) == 0:
        return None
    smallNum = num_list[0]
    for i in num_list:
        if i < smallNum:
            smallNum = i
    return smallNum


    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """

    pass
