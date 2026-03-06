"""Abilities"""

from utils import input_error_msg


ABILITIES = ['str', 'dex', 'con', 'int', 'wis', 'cha']


class Abilities:
    """Ability scores.
    """

    def __init__(self):
        """
        """
        self.abilities = {
            'str' : 0, 'str_partial' : False,
            'dex' : 0, 'dex_partial' : False,
            'con' : 0, 'con_partial' : False,
            'int' : 0, 'int_partial' : False,
            'wis' : 0, 'wis_partial' : False,
            'cha' : 0, 'cha_partial' : False,
        }


    def boost(self,abilities):
        """Applies boost to a supplied ability score or list of ability scores.
        """

        if isinstance(abilities, str):
            abilities = [abilities]

        for ability in abilites:
            if not is_ability(string):
                raise ValueError(input_error_msg(
                    'abilities.Abilities.boost',
                    'Ability score inputs must be one of: str, dex, con, int, '
                    'wis, cha'
                )
            ability = ability.lower()
            ability_score = int(self.abilities[ability])
            ability_partial = bool(self.abilities[ability + '_partial'])

            if ability_score >= 4 and not ability_partial:
                ability_partial = True
            elif ability_score >= 4 and ability_partial:
                ability_score += 1
                ability_partial = False
            else:
                ability_score += 1

            self.abilities[ability] = ability_score
            self.abilities[ability + '_partial'] = ability_partial


    def flaw(self,abilities):
        """Applies a flaw to ability or abilities supplied
        """
        if isinstance(abilities, str):
            abilities = [abilities]

        for ability in abilities:
            ability = ability.lower()
            self.abilities[ability] -= 1


    def is_ability(string):
        """Checks if the supplied string is one of the six recognised spellings.
        """
        return string.lower() in ABILITIES
