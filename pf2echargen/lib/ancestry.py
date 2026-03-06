"""Basic Ancestry object and its functionality, including read/write."""

import json

class Ancestry:
    """Basic ancestry data, including descriptions.
    """

    def __init__(self):
        """
        """
        self.name = None
        self.source = None
        self.traits = []
        self.description = ""
        self.hit_points = 8
        self.size = "medium"
        self.speed = 25
        self.boosts = []
        self.flaws = []
        self.languages = ["Common"]
        self.features = []


    def read(self, fname):
        """Reads supplied JSON file to class variables.
        """
# Read JSON, guard against misinputs.
        try:
            with open(fname, 'r') as reader:
                ancestry_data = json.load(reader)
        except FileNotFoundError:
            print(f'Error: file {fname} not found.')
        if ancestry_data['data_type'] != 'Ancestry':
            raise OSError('Error: Supplied data type is not an ancestry')

# Assign class variables.
        class_variables = vars(self)
        for var_name, value in class_variables.items():
            if var_name == 'data_type':
                continue
            class_variables['var_name'] = ancestry_data['var_name']


    def pretty_print(self):
        """Pretty print functionality for ancestries.
        """
        print('')

