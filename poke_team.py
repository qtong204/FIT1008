import copy
from data_structures.sorted_list_adt import ListItem
from pokemon import *
import random
import math
from typing import List
from data_structures.stack_adt import ArrayStack
from battle_mode import BattleMode
from data_structures.array_sorted_list import ArraySortedList
from data_structures.queue_adt import CircularQueue
from battle_mode import BattleMode



class PokeTeam:
    random.seed(20)
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        """to initialise the team. This takes some additional arguments to determine how initialisation occurs."""
        self.original = ArrayR(self.TEAM_LIMIT)

        self.criterion = None
        self.team = None
        
        self.team_count = 0
        self.fainted1 = None
        self.fainted2 = None
        

        def choose_manually(self):
            """to let the user choose upto 6 Pokemon. Please note that the user 
            should have an option to choose less than 6 Pokemon if they choose to do so
            """

            self.original = ArrayR(int(input('Enter the number of pokemon you want in your team ( maximum is 6 ): ')))
            for i in range(len(self.team)):
                choose_pokemon = int(input('Enter the no of the pokemon you want to add to your team: '))   
                chosen_type = self.POKE_LIST[choose_pokemon]
                pokemon = chosen_type()

                self.team[i] = pokemon
                self.original[i] = pokemon


        
        

    def choose_randomly(self) -> None:
        """to generate a team of 6 randomly chosen Pokemon
        comlpecity: best case : O(1)
                    worst case : O(n + n(c + r)) as n is the number of pokemon in the team, c is the random.choice and r is the random pokemon"""
                
        self.team = ArrayR(self.TEAM_LIMIT)
        for i in range(self.TEAM_LIMIT):#O(n)
            random_pokemon = random.choice(self.POKE_LIST) # O(c)
            self.team[i] = random_pokemon() # O(r)

            self.original[i] = random_pokemon()

    


    def regenerate_team(self, battle_mode: BattleMode) -> None:
        """to heal all of the pokemon to their original HP while preserving their level and evolution.
          This should also assemble the team according to the battle mode (discussed later)
          best case: O(1)
          worst case: O(n), where n is the number of pokemon in the team"""
        
        if battle_mode.name == 'SET':
            temp_stack = ArrayStack(len(self.team)) 
            for i in range(len(self.team)-1 , -1, -1): # O(n)
                pokemon = self.team.pop() # O(1)
                
                pokemon.health = self.original[i].get_health() # O(1)
                temp_stack.push(pokemon) # O(1)
                 
            for i in range(len(temp_stack)): # O(n)
                self.team.push(temp_stack.pop()) # O(1)
        
        elif battle_mode.name == 'ROTATE':
            temp_ori = self.original
            tempp = CircularQueue(len(self.original))
            
            for i in range(len(self.team)):
                pokemon = self.team.serve() # this is the pokemon in the self.team, which is use for battle and so on , O(n)

                for j in range(len(temp_ori)): # O(n)

                    pokemon2 = temp_ori[j] # this is the pokemon in the self.original, which is the original pokemon didnt change before , O(1)

                    if pokemon.get_name() in pokemon2.get_evolution(): # if the pokemon(self.team) is in the evolution of the pokemon(self.original), O(1)
                        pokemon.health = pokemon2.get_health() # O(1)
                        temp_ori[j] = pokemon # O(1)
            
            for i in temp_ori: # O(n)
                tempp.append(i) # O(1)
            
            self.team = tempp # O(1)
            # print(self.team)
            
            
      

    def __getitem__(self, index: int):
        """to retrieve a Pokemon at a specific index of the team
        best case: O(1)
        worst case: O(n), where n is the number of pokemon in the team"""
        if type(self.team) == ArrayStack:
            return self.team.pop()
        elif type(self.team) == CircularQueue:
            return self.team.serve()
        elif type(self.team) == ArraySortedList:
            return self.team[index].value
        return self.original[index]


    def __len__(self):
        """should return the current length of the team
        """
        return len(self.team)
    
    def assemble_team(self, battle_mode: BattleMode):
        """to place your pokemon in the appropriate ADT when a battle mode is selected 
        (you will need to leave this empty right now but you will fill this in later in the next task)
        best case: O(1)
        worst case: O(n), where n is the number of pokemon in the team"""
        if battle_mode.name == 'SET':
            temp_stack = ArrayStack(len(self.team))
            for i in range(len(self.team)): # O(n)
                temp_stack.push(self.team[i]) # O(1)
            self.team = temp_stack
                

        elif battle_mode.name == 'ROTATE':
            temp_queue = CircularQueue(len(self.team)) # O(1)
            for i in range(len(self.team)): # O(n)
                
                temp_queue.append(self.team[i]) # O(1)
                
            self.team = temp_queue
            

    def assign_team(self, criterion: str = None) -> None:
        '''
        best case: O(n)
        worst case: O(nlogn), where n is the number of pokemon in the team
        when add the pokemon to the temp_ArraySortedList it will take O(log(n)) and the loop will take O(n)'''
        temp_ArraySortedList = ArraySortedList(len(self.team))

        if criterion not in self.CRITERION_LIST:
            raise ValueError('Invalid criterion')
        elif criterion == 'health':
            for i in range(len(self.team)): # O(n)
                temp_ArraySortedList.add(ListItem(self.team[i], self.team[i].get_health())) 
        
        elif criterion == 'defence':
            for i in range(len(self.team)):
                temp_ArraySortedList.add(ListItem(self.team[i], self.team[i].get_defence())) 

        elif criterion == 'battle_power':
            for i in range(len(self.team)):
                temp_ArraySortedList.add(ListItem(self.team[i], self.team[i].get_battle_power()))
        
        elif criterion == 'speed':
            for i in range(len(self.team)):
                temp_ArraySortedList.add(ListItem(self.team[i], self.team[i].get_speed()))

        elif criterion == 'level':
            for i in range(len(self.team)):
                temp_ArraySortedList.add(ListItem(self.team[i], self.team[i].get_level()))

                
        self.team = temp_ArraySortedList
        self.criterion = criterion


    def special(self, battle_mode:BattleMode):
        """
        which takes different effects based on the type of battle, which will be covered in the next task
        best case: O(n)
        worst case: O(n), where n is the number of pokemon in the team
        """
        
        if battle_mode.name == 'SET':
            length = len(self.team) # O(n), which the L is the length of the team

            temp_queue = CircularQueue(length) # O(n)
            temp_stack = ArrayStack(length) # O(n)

            for _ in range(length//2): # O(n/2)
                temp_queue.append(self.team.pop()) # O(1)

            for _ in range(length//2): # O(L/2)
                temp_stack.push(self.team.pop()) # O(1)

            for _ in range(length//2): # O(n/2)
                self.team.push(temp_stack.pop()) # O(1) 
            for _ in range(length//2):  # O(n/2)
                self.team.push(temp_queue.serve()) # O(1)
            return self.team
            # self.team = self.stack # original is self.stack
            
        
        elif battle_mode.name == 'ROTATE':
            
            length = len(self.team) # O(n), which the L is the length of the team
            temp_stack = ArrayStack(len(self.team)) # O(n)
            temp_queue = CircularQueue(len(self.team)) # O(n)

            for _ in range(length//2): # O(n/2) 
                temp_queue.append(self.team.serve()) # serve the first half to the temp_queue # O(1)
            for _ in range(length//2): # O(n/2)
                temp_stack.push(self.team.serve()) # serve the second half to the temp_stack # O(1)
            for _ in range(length//2): # O(n/2)
                temp_queue.append(temp_stack.pop()) # O(1)
            
            self.team = temp_queue  
            
            return self.team

        elif battle_mode.name == 'OPTIMISE':

            temp_sortedArrayList = ArraySortedList(len(self.team))
            if self.criterion == 'health':
                for pokemon in self.team:
                    temp_sortedArrayList.add(ListItem(pokemon.value, -pokemon.value.get_health()))
                
            elif self.criterion == 'defence':
                for pokemon in self.team:
                    temp_sortedArrayList.add(ListItem(pokemon.value, -pokemon.value.get_defence()))
            
            elif self.criterion == 'battle_power':
                for pokemon in self.team:
                    temp_sortedArrayList.add(ListItem(pokemon.value, -pokemon.value.get_battle_power()))

            elif self.criterion == 'speed':
                for pokemon in self.team:
                    temp_sortedArrayList.add(ListItem(pokemon.value, -pokemon.value.get_speed()))

            elif self.criterion == 'level':
                for pokemon in self.team:
                    temp_sortedArrayList.add(ListItem(pokemon.value, -pokemon.value.get_level()))
                

            self.team = temp_sortedArrayList

            
            

        
    def __str__(self):
        """ should print out the current members of the team with each member printed in a new line"""
        team_members = "\n".join(str(pokemon) for pokemon in self.original)
        return team_members



class Trainer:

    def __init__(self, name) -> None:
        """which should take the name as an argument and set the Trainer's name, 
        initialise a new PokeTeam and also a Pokedex. """
        self.name = name
        self.PokeTeam = PokeTeam()
        self.pokedex = ArrayR(len(PokeType))


    def pick_team(self, method: str) -> None:
        """which should pick a team based on the mode that is supplied to the method as an argument. 
        Pick team can only have the values 'Random' or 'Manual'.
        You should return an error if one of these options is not chosen
        best case: O(1)
        worst case: O(n)"""
        method = method.upper()
        if method == 'RANDOM':
            return self.PokeTeam.choose_randomly() 
        elif method == 'MANUAL':
            return self.PokeTeam.choose_manually()
        else:
            raise ValueError('Invalid method')


    def get_team(self) -> PokeTeam:
        """which should return the current PokeTeam
        best case : O(1)
        worst case : O(1)
        """
        return self.PokeTeam

    def get_name(self) -> str:
        """best case : O(1)
        worst case : O(1)"""
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        """which should register a pokemon as seen on the trainer's Pokedex
        best case : O(1)
        worst case : O(1)"""
        if  self.pokedex[pokemon.get_poketype().value] is None:
            self.pokedex[pokemon.get_poketype().value] = pokemon.get_poketype()

        # raise ValueError('Pokedex is full')
        
    def get_pokedex_completion(self) -> float:
        """which should return a rounded float ratio of the number of different 
        TYPES of pokemon seen vs the total number of TYPES of pokemon available rounded to 2 decimal points. 
        For this point, two FIRE type pokemon count as the exact same
        best case : O(1)
        worst case : O(n), where the n is the number of pokemon in the pokedex""" 
        # the datatype should be used as set which their items are not repeated
        length_of_pokedex = 0
        for i in range(len(self.pokedex)): # O(n)
            if self.pokedex[i] != None: # O(1)
                length_of_pokedex += 1 # O(1)

                
        return round((length_of_pokedex / len(PokeType)), 2) # O(1)
        

    def __str__(self) -> str:
        """should return a string of the following format: Trainer <trainer_name> Pokedex Completion: <completion>%
You need to convert your pokedex completion to a percentage here by multiplying it by 100"""
        return f'Trainer {self.name} Pokedex Completion: {int(self.get_pokedex_completion() * 100)}%'

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")




