"""
Exercise 11
"""


def get_hr_min_sec(inputSec):
    result = ''
    sec = inputSec % 60
    min = (inputSec // 60) % 60
    hour = inputSec // 3600
    if inputSec == 0:
        return '0s'
    if sec > 0:
        result = str(sec) + 's '
    if min > 0:
        result = str(min) + 'm ' + result
    if hour > 0:
        result = str(hour) + 'h ' + result
    return result.strip()


    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    pass
