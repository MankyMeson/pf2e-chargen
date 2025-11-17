"""Base character class and supporting functions"""


from abilities import Abilities


class Character():
    """Defines all aspects of a character.

    Highest level data structure created by this package, through which the
    user interacts with the program.
    """


    def __init__(self):
        """
        """
# Personal details.
        self.name = 'Unnamed Adventurer'
        self.size = None

# ABCs.
        self.ancestry = None
        self.background = None
        self.class = None

# Stats and proficiencies.
        self.ability_scores = Abilities()
        self.proficiencies = None
        self.languages = ['Common']
        self.features = []


    def set_ancestry(self, ancestry):
        pass
