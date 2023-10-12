"""
Exercise 20 : Leap Year
"""


def is_leap_year(year):
    if year %400 == 0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 ==0:
        return True
    else:
        return False



    """
    Check if the given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # fix : complete this
    pass
