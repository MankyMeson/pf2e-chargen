"""Command line interface for PF2e Chargen

Contains means of interacting with the program via the command line.
"""

from lib import random


def main():
    """Main function, contains the CLI loop.
    """
    print('Hello world')
    print(f'{random.d20()}')
