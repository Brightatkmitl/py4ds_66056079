"""
Exercise 16
"""


def mode(num_list):
    numLen = len(num_list)
    if numLen == 0:
        return None
    maxCount = 0
    numFreq= 0
    for i in range(0, numLen):
        count = 0
        for j in range(0, numLen):
            if num_list[i] == num_list[j]:
                count += 1
        if count > maxCount:
            maxCount = count
            numFreq = num_list[i]

    return numFreq
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    pass
