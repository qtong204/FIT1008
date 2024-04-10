from data_structures.sorted_list_adt import ListItem
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode
import random
import math
from data_structures.queue_adt import CircularQueue



class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.battle_mode = battle_mode
        self.criterion = criterion

    

    def commence_battle(self) -> Trainer | None:
        """which calls the appropriate battle method from the 3 based on the battle mode set in the initialiser. 
        This method returns the winning trainer or None; in the case when its a draw"""
        temp_fainted1 = CircularQueue(6)
        temp_fainted2 = CircularQueue(6)
        winner = None

        if self.battle_mode.name == "SET":

            
            pokemon_1 = self.trainer_1.get_team().team.pop() # pop the pokemon from the team


            self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon

            pokemon_2 = self.trainer_2.get_team().team.pop() # pop the pokemon from the team

            self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon

            while winner == None:
                self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon
                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon

                if pokemon_1.speed > pokemon_2.speed:
                    if pokemon_2.health > 0:

                        pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))

                        if pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            
                            if self.check_winner() == None:
                                pokemon_2 = self.trainer_2.get_team().team.pop() # if there is no winner the next pokemon will be poped from the team (which the pokemon health is >=0, then can pop for the next pokemon)
                                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
                            
                            elif self.check_winner() != None: # if there is a winner 

                                if pokemon_1.health > 0: # when the last pokemon that we fight with is still alive, then we need to push back to the team
                                    self.trainer_1.get_team().team.push(pokemon_1)

                                winner = self.check_winner() # use the method that I create to check the winner the return the trainer 
                                
                                return winner
                            
                        elif pokemon_2.health > 0: # if the pokemon health is greater than 0, then the pokemon will attack the other pokemon
                            pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))

                            if pokemon_1.health <= 0: # if the pokemon health is less than or equal to 0, then the pokemon will level up
                                pokemon_2.level_up() 

                                if self.check_winner() == None: 
                                    pokemon_1 = self.trainer_1.get_team().team.pop()
                                    self.trainer_2.register_pokemon(pokemon_1)
                                else:
                                    if pokemon_2.health > 0:
                                        self.trainer_2.get_team().team.push(pokemon_2)
                                    winner = self.check_winner()
                                    return winner
                                
                            elif pokemon_1.health > 0 and pokemon_2.health > 0: # if they both survive after both attack, their health will be reduced by 1 

                                pokemon_2.health = pokemon_2.get_health() - 1
                                pokemon_1.health = pokemon_1.get_health() - 1

                                if pokemon_1.health > 0 and pokemon_2.health <= 0: # then check each situation, whether is the pokemon health is greater than 0 or less than 0
                                    pokemon_1.level_up()
                                    
                                    if self.check_winner() == None:
                                        pokemon_2 = self.trainer_2.get_team().team.pop()
                                        self.trainer_1.register_pokemon(pokemon_2)
                                    else:
                                        if pokemon_1.health > 0:
                                            self.trainer_1.get_team().team.push(pokemon_1)
                                        winner = self.check_winner()
                                        return winner
                                    
                                elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                    pokemon_2.level_up()

                                    if self.check_winner() == None:
                                        pokemon_1 = self.trainer_1.get_team().team.pop()
                                        self.trainer_2.register_pokemon(pokemon_1)
                                    else:
                                        if pokemon_2.health > 0:
                                            self.trainer_2.get_team().team.push(pokemon_2)
                                        winner = self.check_winner()
                                        return winner
                                
                    
                    

                elif pokemon_1.speed < pokemon_2.speed: # same as above just the direction all change 
                    if pokemon_1.health > 0:
                        pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))

                        if pokemon_1.health <= 0:
                            pokemon_2.level_up()

                            if self.check_winner() == None:
                                pokemon_1 = self.trainer_1.get_team().team.pop()
                                self.trainer_2.register_pokemon(pokemon_1)
                            elif self.check_winner() != None:
                                if pokemon_2.health > 0:
                                    self.trainer_2.get_team().team.push(pokemon_2)
                                
                                winner = self.check_winner()
                                return winner
                            
                        elif pokemon_1.health > 0:
                            pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))


                            if pokemon_2.health <= 0:
                                pokemon_1.level_up()

                                if self.check_winner() == None:
                                    pokemon_2 = self.trainer_2.get_team().team.pop()
                                    self.trainer_1.register_pokemon(pokemon_2)
                                elif self.check_winner() != None:
                                    if pokemon_1.health > 0:
                                        self.trainer_1.get_team().team.push(pokemon_1)
                                    winner = self.check_winner()
                                    return winner
                                
                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                                pokemon_1.health = pokemon_1.get_health() - 1
                                pokemon_2.health = pokemon_2.get_health() - 1

                                if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                    pokemon_1.level_up()

                                    if self.check_winner() == None:
                                        pokemon_2 = self.trainer_2.get_team().team.pop()
                                        self.trainer_1.register_pokemon(pokemon_2)
                                    elif self.check_winner() != None:
                                        if pokemon_1.health > 0:
                                            self.trainer_1.get_team().team.push(pokemon_1)
                                        winner = self.check_winner()
                                        return winner
                                    
                                elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                    pokemon_2.level_up()

                                    if self.check_winner() == None:
                                        pokemon_1 = self.trainer_1.get_team().team.pop()
                                        self.trainer_2.register_pokemon(pokemon_1)

                                    elif self.check_winner() != None:
                                        if pokemon_2.health > 0:
                                            self.trainer_2.get_team().team.push(pokemon_2)                                     
                                        winner = self.check_winner()
                                        return winner
                                    
                elif pokemon_1.speed == pokemon_2.speed: # when their speed are the same, then they will attack each other
                    
                    # first attack is here 
                    pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                    pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))


                    

                    if pokemon_1.health > 0 and pokemon_2.health > 0: # if they both survive after both attack, their health will be reduced by 1
                        pokemon_1.health = pokemon_1.get_health() - 1
                        pokemon_2.health = pokemon_2.get_health() - 1
                        
                        if pokemon_1.health > 0 and pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            if self.check_winner() == None:
                                pokemon_2 = self.trainer_2.get_team().team.pop()
                                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
                            elif self.check_winner() != None:
                                if pokemon_1.health > 0:
                                    self.trainer_1.get_team().team.push(pokemon_1)
                                winner = self.check_winner()
                                return winner

                            
                            # pokemon 2 should be back
                        elif pokemon_1.health <= 0 and pokemon_2.health > 0: # if the pokemon 1 health is less than or equal to 0 and the pokemon 2 health is greater than 0
                            pokemon_2.level_up()
                            if self.check_winner() == None: # check the winner again then if no winner we pop from the team which pokemon who is fainted and let the opposite to register the pokemon
                                pokemon_1 = self.trainer_1.get_team().team.pop()
                                self.trainer_2.register_pokemon(pokemon_1)
                            elif self.check_winner() != None: # if there is a winner
                                if pokemon_2.health > 0: # the last pokemon which is still alive will be push back to the team
                                    self.trainer_2.get_team().team.push(pokemon_2)
                                winner = self.check_winner()
                                return winner

                            
                            # pokemon 1 should be back
                        elif pokemon_1.health <= 0 and pokemon_2.health <= 0: # after both attack then both health is less than or equal to 0
                            if self.check_winner() == None:
                                pokemon_1 = self.trainer_1.get_team().team.pop()
                                self.trainer_2.register_pokemon(pokemon_1)
                                pokemon_2 = self.trainer_2.get_team().team.pop()
                                self.trainer_1.register_pokemon(pokemon_2)
                                
                            elif self.check_winner() != None:
                                winner = self.check_winner()
                                return winner
                            
                                 

                    elif pokemon_1.health > 0 and pokemon_2.health <= 0:
                        pokemon_1.level_up()

                        if self.check_winner() == None:
                            pokemon_2 = self.trainer_2.get_team().team.pop()
                            self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
                        elif self.check_winner() != None:
                            if pokemon_1.health > 0:
                                self.trainer_1.get_team().team.push(pokemon_1)
                            winner = self.check_winner()
                            return winner
                        
                    elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                        pokemon_2.level_up()

                        if self.check_winner() == None:
                            pokemon_1 = self.trainer_1.get_team().team.pop()
                            self.trainer_2.register_pokemon(pokemon_1)
                        elif self.check_winner() != None:
                            if pokemon_2.health > 0:
                                self.trainer_2.get_team().team.push(pokemon_2)
                            winner = self.check_winner()
                            return winner                        

                    elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
 
                        if self.check_winner() == None:
                            pokemon_1 = self.trainer_1.get_team().team.pop()
                            self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon

                            pokemon_2 = self.trainer_2.get_team().team.pop()
                            self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon

                        elif self.check_winner() != None:
                            winner = self.check_winner()
                            return winner
                # winner = None
        elif self.battle_mode.name == "ROTATE":
            """this is make use of the CircularQueue to rotate the pokemon from the team of the trainer, and after two pokemons fight then change the next group of pokemon to fight
            best case : O(1), when there is onlu oen pokemon each team
            worst case : O(n), as n in the length of the team of the trainer"""


            
            for i,j in zip(self.trainer_1.get_team().original, self.trainer_2.get_team().original):
                self.trainer_1.register_pokemon(i)
                self.trainer_2.register_pokemon(j)

            while winner is None: # make use of the while loop to check the winner, stop when find the winner, O(n)
                
                winner = self.check_winner()
                print(len(self.trainer_1.get_team().team))
                print(len(self.trainer_2.get_team().team))
                if winner != None: # if there is a winner then return the trainer (winner)
                    
                    return winner
 
                pokemon_1 = self.trainer_1.get_team().team.serve() # serve t he pokemon from the CircularQueue
                pokemon_2 = self.trainer_2.get_team().team.serve() # serve the pokemon from the CircularQueue

                print(f'{pokemon_1} {pokemon_1.get_speed()} {self.trainer_1.get_pokedex_completion()}')
                print(f'{pokemon_2} {pokemon_2.get_speed()} {self.trainer_2.get_pokedex_completion()}')

                
                
                self.trainer_1.register_pokemon(pokemon_2) # let the opponent to register the pokemon
 
                self.trainer_2.register_pokemon(pokemon_1) # let the opponent to register the pokemon
 
                if pokemon_1.speed > pokemon_2.speed:
                    pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))
                    print(pokemon_1.health)
                    print(pokemon_2.health)
                    if pokemon_2.health <= 0 and pokemon_1.health > 0:
                        pokemon_1.level_up()
                        self.trainer_1.get_team().team.append(pokemon_1)

                        
                        

                        print(pokemon_1.health)
                        print(pokemon_2.health)
                        
                        # here should procide to the next battle 
                    elif pokemon_2.health > 0:
                        pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                        print(pokemon_1.health)
                        print(pokemon_2.health)
                        if pokemon_1.health <= 0 and pokemon_2.health > 0:
                            pokemon_2.level_up() 
                        
                            self.trainer_2.get_team().team.append(pokemon_2)
                            
                            
                            
                            print(pokemon_1.health)
                            print(pokemon_2.health)
                        elif pokemon_1.health > 0 and pokemon_2.health > 0: # Whhen they both survive after both attack, their health will be reduced by 1
                            pokemon_1.health = pokemon_1.get_health() - 1
                            pokemon_2.health = pokemon_2.get_health() - 1
                            print(pokemon_1.health)
                            print(pokemon_2.health)
                            
                            if pokemon_1.health > 0 and pokemon_2.health <= 0: # then check each situation, whether is the pokemon health is greater than 0 or less than 0
                                pokemon_1.level_up()
                                self.trainer_1.get_team().team.append(pokemon_1) # then the pokemon who health > 0 will be append back to the team
                            
                                
                                print(pokemon_1.health)
                                print(pokemon_2.health)
                            elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                pokemon_2.level_up()
                                
                                self.trainer_2.get_team().team.append(pokemon_2)
                                
                                

                                print(pokemon_1.health)
                                print(pokemon_2.health)
                            elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                                
                                continue

                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                            
                                self.trainer_1.get_team().team.append(pokemon_1)
                                self.trainer_2.get_team().team.append(pokemon_2)
                                print(pokemon_1.health)
                                print(pokemon_2.health)
                                
                elif pokemon_1.speed < pokemon_2.speed: # same logic as above just change the direction only
                    
                    pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                    print(pokemon_1.health)
                    print(pokemon_2.health)
                    if pokemon_1.health <= 0 and pokemon_2.health > 0:
                        pokemon_2.level_up()
                        self.trainer_2.get_team().team.append(pokemon_2)
                        
                        
                        print(pokemon_1.health)
                        print(pokemon_2.health)

                    elif pokemon_1.health > 0:
                        pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))
                        print(pokemon_1.health)
                        print(pokemon_2.health)
                        if pokemon_2.health <= 0 and pokemon_1.health > 0:
                            pokemon_1.level_up()
                            self.trainer_1.get_team().team.append(pokemon_1)
                            
                            
                             
                            print(pokemon_1.health)
                            print(pokemon_2.health)
                        elif pokemon_1.health > 0 and pokemon_2.health > 0:
                            pokemon_1.health = pokemon_1.get_health() - 1
                            pokemon_2.health = pokemon_2.get_health() - 1
                            
                            print(pokemon_1.health)
                            print(pokemon_2.health)
                            if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                pokemon_1.level_up()
                                self.trainer_1.get_team().team.append(pokemon_1)
                                
                                
                            
                                print(pokemon_2.health)
                                
                            elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                pokemon_2.level_up()
                                
                                self.trainer_2.get_team().team.append(pokemon_2)
                                
                                
                                
                                print(pokemon_1.health)
                                print(pokemon_2.health)

                                
                            elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                                continue
                                
                                

                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                                self.trainer_1.get_team().team.append(pokemon_1)
                                self.trainer_2.get_team().team.append(pokemon_2)
                                
                                print(pokemon_1.health)
                                print(pokemon_2.health)

                elif pokemon_1.speed == pokemon_2.speed:
                    pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                    pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))
                    if pokemon_1.health > 0 and pokemon_2.health > 0:
                        pokemon_1.health = pokemon_1.get_health() - 1
                        pokemon_2.health = pokemon_2.get_health() - 1
                        if pokemon_1.health > 0 and pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            self.trainer_1.get_team().team.append(pokemon_1)
                            
                            

                        elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                            pokemon_2.level_up()
                            self.trainer_2.get_team().team.append(pokemon_2)
                            
                        

                        elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                            
                            continue

                    elif pokemon_1.health > 0 and pokemon_2.health <= 0:
                        pokemon_1.level_up()
                        self.trainer_1.get_team().team.append(pokemon_1)
                        
                        

                    elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                        pokemon_2.level_up()
                        self.trainer_2.get_team().team.append(pokemon_2)
                        
                        

                    elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                        continue
                        

        elif self.battle_mode.name == "OPTIMISE":
            
            while winner == None:
                
                winner = self.check_winner()
                if winner != None:
                    return winner

                pokemon_1 = self.trainer_1.get_team().team.delete_at_index(0).value # delete the pokemon from the team, which give us the pokemon that we want to fight with
                

                pokemon_2 = self.trainer_2.get_team().team.delete_at_index(0).value
                

                self.trainer_1.register_pokemon(pokemon_2)
                self.trainer_2.register_pokemon(pokemon_1)
                if pokemon_1.speed > pokemon_2.speed:
                    pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))
                    if pokemon_2.health <= 0:
                        pokemon_1.level_up()
                        self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                    elif pokemon_2.health > 0:
                        
                        pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                       
                        if pokemon_1.health <= 0:
                            pokemon_2.level_up()
                            self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))
                        
                        elif pokemon_1.health > 0 and pokemon_2.health > 0:
                            pokemon_1.health = pokemon_1.get_health() - 1
                            pokemon_2.health = pokemon_2.get_health() - 1
                            
                            if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                pokemon_1.level_up()
                                self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))

                            elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                pokemon_2.level_up()
                                self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))

                            elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                                continue

                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                                
                                self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                                self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))
                
                elif pokemon_1.speed < pokemon_2.speed:
                    pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                    

                    if pokemon_1.health <= 0:
                        pokemon_2.level_up()
                        self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))
                    elif pokemon_1.health > 0:
                        pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))
                       

                        if pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))

                        elif pokemon_1.health > 0 and pokemon_2.health > 0:
                            pokemon_1.health = pokemon_1.get_health() - 1
                            pokemon_2.health = pokemon_2.get_health()
                            

                            if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                pokemon_1.level_up()
                                self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))

                            elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                pokemon_2.level_up()
                                self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))

                            elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                                continue

                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                                
                                self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                                self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))
                
                elif pokemon_1.speed == pokemon_2.speed:
                    pokemon_1.defend(math.ceil(pokemon_2.attack(pokemon_1) * (self.trainer_2.get_pokedex_completion() / self.trainer_1.get_pokedex_completion())))
                    pokemon_2.defend(math.ceil(pokemon_1.attack(pokemon_2) * (self.trainer_1.get_pokedex_completion() / self.trainer_2.get_pokedex_completion())))

                    if pokemon_1.health > 0 and pokemon_2.health > 0:
                        pokemon_1.health = pokemon_1.get_health() - 1
                        pokemon_2.health = pokemon_2.get_health() - 1
                        if pokemon_1.health > 0 and pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                        elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                            pokemon_2.level_up()
                            self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))
                        elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                            continue
                    elif pokemon_1.health > 0 and pokemon_2.health <= 0:
                        pokemon_1.level_up()
                        self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                    elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                        pokemon_2.level_up()
                        self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))

                    elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                        continue
                    elif pokemon_1.health > 0 and pokemon_2.health > 0:
                        self.trainer_1.get_team().team.add(ListItem(pokemon_1, pokemon_1.get_health()))
                        self.trainer_2.get_team().team.add(ListItem(pokemon_2, pokemon_2.get_health()))






                    
                
    def check_winner(self) -> Trainer | None:
        
        if len(self.trainer_1.get_team().team) == 0 and len(self.trainer_2.get_team().team) == 0:
            return None
        elif len(self.trainer_1.get_team().team) == 0: # so is like I change the len of the team, if the team is become zero means that the opponent win
            
            return self.trainer_2
        
        elif len(self.trainer_2.get_team().team) == 0:
            return self.trainer_1
        
        
        return None
    


    def _create_teams(self) -> None:

        self.trainer_1.pick_team('Random')
        self.trainer_2.pick_team('Random')
        """which turns the PokeTeams from the two trainers into appropriate data structures based on the mode supplied to the battle as an initial argument."""
        if self.battle_mode.name == "SET":
            self.trainer_1.get_team().assemble_team(self.battle_mode)
            for i in self.trainer_1.get_team().original:
                self.trainer_1.register_pokemon(i)
            self.trainer_2.get_team().assemble_team(self.battle_mode)
            for i in self.trainer_2.get_team().original:
                self.trainer_2.register_pokemon(i)

        
        elif self.battle_mode.name == "ROTATE":
            self.trainer_1.get_team().assemble_team(self.battle_mode)
            for i in self.trainer_1.get_team().original:
                self.trainer_1.register_pokemon(i)
            self.trainer_2.get_team().assemble_team(self.battle_mode)
            for i in self.trainer_2.get_team().original:
                self.trainer_2.register_pokemon(i)
        
        elif self.battle_mode.name == "OPTIMISE":
            self.trainer_1.get_team().assign_team(self.criterion)
            for i in self.trainer_1.get_team():
                self.trainer_1.register_pokemon(i)
            self.trainer_2.get_team().assign_team(self.criterion)
            for i in self.trainer_2.get_team():
                self.trainer_2.register_pokemon(i)

    




if __name__ == '__main__':
    # test 3.1
    random.seed(20)
    t1 = Trainer('Gary')
    t2 = Trainer('Ash')

    b = Battle(t1, t2, BattleMode.ROTATE)
    b._create_teams()
    # t1.get_team().special(BattleMode.ROTATE)
    print(t1.get_team())
    print('')
    print(t2.get_team())
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
   
    # t2.get_team().regenerate_team(BattleMode.ROTATE)
    



