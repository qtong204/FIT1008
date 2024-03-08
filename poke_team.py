from pokemon import *
import random
from typing import List

class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        """to initialise the team. This takes some additional arguments to determine how initialisation occurs."""
        self.team = []

    def choose_manually(self):
        """to let the user choose upto 6 Pokemon. Please note that the user 
        should have an option to choose less than 6 Pokemon if they choose to do so"""
        pass

    def choose_randomly(self) -> None:
        """to generate a team of 6 randomly chosen Pokemon"""
        pass
       

    def regenerate_team(self) -> None:
        """to heal all of the pokemon to their original HP while preserving their level and evolution. 
        This should also assemble the team according to the battle mode (discussed later)"""
        raise NotImplementedError

    def __getitem__(self, index: int):
        """to retrieve a Pokemon at a specific index of the team"""
        return self.team[index]

    def __len__(self):
        """should return the current length of the team"""
        return len(self.team)
    
    def assemble_team(self):
        pass

    def special(self):
        pass

    def __str__(self):
        """ should print out the current members of the team with each member printed in a new line"""
        for i in range(len(self.team)):
            print(self.team[i])

class Trainer:

    def __init__(self, name) -> None:
        """which should take the name as an argument and set the Trainer's name, 
        initialise a new PokeTeam and also a Pokedex. """
        self.name = name
        self.PokeTeam = None
        self.pokedex = None
        # raise NotImplementedError

    def pick_team(self, method: str) -> None:
        """which should pick a team based on the mode that is supplied to the method as an argument. 
        Pick team can only have the values 'Random' or 'Manual'.
        You should return an error if one of these options is not chosen"""
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        """which should return the current PokeTeam"""
        return self.PokeTeam

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        """which should register a pokemon as seen on the trainer's Pokedex"""
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        """which should return a rounded float ratio of the number of different 
        TYPES of pokemon seen vs the total number of TYPES of pokemon available rounded to 2 decimal points. 
        For this point, two FIRE type pokemon count as the exact same"""
        raise NotImplementedError

    def __str__(self) -> str:
        """should return a string of the following format: Trainer <trainer_name> Pokedex Completion: <completion>%
You need to convert your pokedex completion to a percentage here by multiplying it by 100"""
        raise NotImplementedError

if __name__ == '__main__':
    # t = Trainer('Ash')
    # print(t)
    # t.pick_team("Random")
    # print(t)
    # print(t.get_team())
    pkt = PokeTeam()
    print(pkt.choose_randomly())