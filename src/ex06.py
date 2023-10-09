"""
Execise 6
"""


def ordinal_suffix(num):
    numstr = str(num)

    if numstr[-2:] in ("11","12","13"):
        return numstr + "th"
    elif numstr[-1] == "1":
        return numstr + "st"
    elif numstr[-1] == "2":
        return numstr + "nd"
    elif numstr[-1] == "3":
        return numstr + "rd"
    else:
        return numstr + "th"




    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # fix : complete this
    pass

