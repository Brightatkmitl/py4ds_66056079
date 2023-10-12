"""
Exercise 17
"""
import random


def roll_dice(num_of_dice):
    total = 0
    for i in range(num_of_dice):
        total += random.randint(1,6)
    return total

    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """
    pass
