"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(totalCoffee,price ):
    free = totalCoffee // 9
    pay = totalCoffee - free
    return pay * price
    pass
