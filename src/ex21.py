"""
Exercise 21 : Validate Date

"""


def is_valid_date(year, months, days):

    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here

    from src.ex20 import is_leap_year

    if not (1 <= months <= 12):
        return False
    if is_leap_year(year) and months == 2 and days == 29:
        return True
    if months in (1, 3, 5, 7, 8, 10, 12) and not (1 <= days <= 31):
        return False
    if months in (4, 6, 9, 11) and not (1 <= days <= 30):
        return False
    if months == 2 and not (1 <= days <= 28):
        return False
    return True


    # fix : complete this
    pass
