"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(password_input):
    password = password_input
    if password_input < 12 :
        password = 12
    password1 = [LOWER_LETTERS[random.randint(0, 25)], UPPER_LETTERS[random.randint(0, 25)],
                   NUMBERS[random.randint(0, 9)], SPECIAL[random.randint(0, 12)]]
    while len(password1) < password:
        password1.append(ALL_CHARS[random.randint(0, 74)])
    random.shuffle(password1)
    return ''.join(password1)



    # fix : complete this
    pass
