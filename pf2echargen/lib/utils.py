"""Utilities module for handling run control, string manipulation, and other
unsorted useful things.
"""

import sys

def input_error_msg(function: str, message: str):
    return "Error in data input detected by:\n" + function + "\n\n" + str
