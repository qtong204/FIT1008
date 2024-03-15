from pokemon import *
import random
from typing import List
from data_structures.array_sorted_list import ArraySortedList
class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()

    def __init__(self):
        """to initialise the team. This takes some additional arguments to determine how initialisation occurs."""
        pass
        self.team = None

    def choose_manually(self):
        """to let the user choose upto 6 Pokemon. Please note that the user 
        should have an option to choose less than 6 Pokemon if they choose to do so"""

        self.team = ArrayR(int(input('Enter the number of pokemon you want in your team ( maximum is 6 ): ')))
        for i in range(len(self.team)):
            choose_pokemon = int(input('Enter the no of the pokemon you want to add to your team: '))    
            self.team[i] = self.POKE_LIST[choose_pokemon]()

        return self.team
        

    def choose_randomly(self) -> None:
        """to generate a team of 6 randomly chosen Pokemon"""
        self.team = ArrayR(self.TEAM_LIMIT)
        for i in range(self.TEAM_LIMIT):
            random_pokemon = random.choice(self.POKE_LIST)
            # print(random_pokemon)
            self.team[i] = random_pokemon()
        return str(self.team)
        
       

    def regenerate_team(self) -> None:
        """to heal all of the pokemon to their original HP while preserving their level and evolution. 
        This should also assemble the team according to the battle mode (discussed later)"""
        team_regenerated = self.team
        return team_regenerated

    def __getitem__(self, index: int):
        """to retrieve a Pokemon at a specific index of the team"""
        return self.team[index]

    def __len__(self):
        """should return the current length of the team"""
        return len(self.team)
    
    def assemble_team(self):
        """to place your pokemon in the appropriate ADT when a battle mode is selected 
        (you will need to leave this empty right now but you will fill this in later in the next task)"""
        pass

    def special(self):
        """
        which takes different effects based on the type of battle, which will be covered in the next task
        """
        pass

    def __str__(self):
        """ should print out the current members of the team with each member printed in a new line"""
        team_members = "\n".join(str(pokemon) for pokemon in self.team)
        return team_members



class Trainer:

    def __init__(self, name) -> None:
        """which should take the name as an argument and set the Trainer's name, 
        initialise a new PokeTeam and also a Pokedex. """
        self.name = name
        self.PokeTeam = PokeTeam()
        self.pokedex = ArraySortedList(len(PokeType))


    def pick_team(self, method: str) -> None:
        """which should pick a team based on the mode that is supplied to the method as an argument. 
        Pick team can only have the values 'Random' or 'Manual'.
        You should return an error if one of these options is not chosen"""

        if method == 'Random':
            return self.PokeTeam.choose_randomly()
        elif method == 'Manual':
            return self.PokeTeam.choose_manually()
        else:
            raise ValueError('Invalid method')


    def get_team(self) -> PokeTeam:
        """which should return the current PokeTeam"""
        return self.PokeTeam

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        """which should register a pokemon as seen on the trainer's Pokedex"""
        if pokemon.get_poketype() not in self.pokedex:
            self.pokedex.append(pokemon.get_poketype())
        # pass

        
        
    def get_pokedex_completion(self) -> float:
        """which should return a rounded float ratio of the number of different 
        TYPES of pokemon seen vs the total number of TYPES of pokemon available rounded to 2 decimal points. 
        For this point, two FIRE type pokemon count as the exact same""" 
        # the datatype should be used as set which their items are not repeated
        return len(self.pokedex) / len(PokeType)
        

    def __str__(self) -> str:
        """should return a string of the following format: Trainer <trainer_name> Pokedex Completion: <completion>%
You need to convert your pokedex completion to a percentage here by multiplying it by 100"""
        return f'Trainer {self.name} Pokedex Completion: {self.get_pokedex_completion()}%'

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")

    # print(t.get_team())
    # print(t.PokeTeam)
    # for i in range(len(t.PokeTeam)):
    #     t.register_pokemon(t.PokeTeam[i])
    #     # print(t.PokeTeam[i])
    # print(t.pokedex)
    # print(Pikachu())
    t.register_pokemon(Pikachu())
    # print(t.pokedex)
    print(len(t.pokedex))
    t.register_pokemon(Pidgey())




    