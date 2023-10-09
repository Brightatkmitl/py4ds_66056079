"""
Execise 9
"""


def get_chess_square_color(col, row):
    if col <1 or col > 8 or row <1 or row > 8:
        return " "
    elif col %2 == row %2:
        return "White"
    elif col%2 != row%2:
        return "Black"


    """
    Returns the color of a chess square given its column and row.
    The color of the square is determined by checking
    if the sum of col and row is even or odd.
    If col + row is even, the square is considered White,
    otherwise it is considered Black.

    Parameters:
        col (int): The column of the chess square.
        row (int): The row of the chess square.

    Returns:
        str: The color of the chess square, either 'white' or 'black'.
    """
    # TODO : complete this
    pass
