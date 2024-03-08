from pokemon import *
import random
from typing import List

class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        """to initialise the team. This takes some additional arguments to determine how initialisation occurs."""
        self.index = None
        self.team = None

    def choose_manually(self):
        """to let the user choose upto 6 Pokemon. Please note that the user 
        should have an option to choose less than 6 Pokemon if they choose to do so"""

        choose =  int(input("How many pokemon that you want to choose (1~6): "))
        for i in range(choose):
            choose_pokemon = input("Choose a pokemon: ")
            if choose_pokemon in self.POKE_LIST:
                self.team.append(choose_pokemon)
            
        return self.team

        

    def choose_randomly(self) -> None:
        """to generate a team of 6 randomly chosen Pokemon"""
        raise NotImplementedError

    def regenerate_team(self) -> None:
        """to heal all of the pokemon to their original HP while preserving their level and evolution. 
        This should also assemble the team according to the battle mode (discussed later)"""
        raise NotImplementedError

    def __getitem__(self, index: int):
        """to retrieve a Pokemon at a specific index of the team"""
        raise NotImplementedError

    def __len__(self):
        """should return the current length of the team"""
        raise NotImplementedError

    def __str__(self):
        """ should print out the current members of the team with each member printed in a new line"""
        raise NotImplementedError

class Trainer:

    def __init__(self, name) -> None:
        raise NotImplementedError

    def pick_team(self, method: str) -> None:
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def register_pokemon(self, pokemon: Pokemon) -> None:
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())