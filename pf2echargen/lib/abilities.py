"""Abilities"""


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


    def boost(abilities):
        """Applies boost to a supplied ability score or list of ability scores.
        """

        if isinstance(abilities, str):
            abilities = [abilities]

        for ability in abilites:
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


    def flaw(abilities):
        """Applies a flaw to ability or abilities supplied
        """
        if isinstance(abilities, str):
            abilities = [abilities]

        for ability in abilities:
            ability = ability.lower()
            self.abilities[ability] -= 1

