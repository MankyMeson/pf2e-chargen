"""Random number generation functions"""


import random


def d20():
    """
    """
    return random.randrange(1, 21)

def d10():
    return random.randrange(1, 11)

def d8():
    return random.randrange(1, 9)

def d6():
    return random.randrange(1, 7)

def d4():
    return random.randrange(1, 5)

def d3():
    return random.randrange(1, 4)
