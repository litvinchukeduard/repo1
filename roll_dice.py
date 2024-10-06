import random
"""
Написати функцію, яка буде симулювати кидання кубиків
"""

def roll_dice() -> tuple: # (1, 6) (6, 1)
    """ Function that simulates a roll of the dice """
    # print(random.randint(1, 6))
    # result = (random.randint(1, 6), random.randint(1, 6))
    # return result
    return (random.randint(1, 6), random.randint(1, 6))

print(roll_dice())
print(roll_dice())
print(roll_dice())
