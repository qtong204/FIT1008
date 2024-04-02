from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode
import random



class Battle:

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.battle_mode = battle_mode
        self.criterion = criterion

    

    def commence_battle(self) -> Trainer | None:
        """which calls the appropriate battle method from the 3 based on the battle mode set in the initialiser. 
        This method returns the winning trainer or None; in the case when its a draw"""
        # while len(self.trainer_1.get_team()) > 0 and len(self.trainer_2.get_team()) > 0:
        winner = None
        if self.battle_mode.name == "SET":
            # faint_team = Arrayteam(len(self.trainer_1.get_team()))
            
            pokemon_1 = self.trainer_1.get_team().team.pop()

            # self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon
            
           
            pokemon_2 = self.trainer_2.get_team().team.pop()

            self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
            print(f'team 1 {self.trainer_1.get_team()}')
            print('\n')
            print(f'team 2 {self.trainer_2.get_team().team}')
            print('\n')

            while winner == None:
                # print(f'pokemon1  : {pokemon_1} and poketype is {pokemon_1.get_poketype()}')
                print(f'{pokemon_1}  {pokemon_1.get_speed()}')
                
                # print(f'pokemon2  : {pokemon_2} and poketype is {pokemon_2.get_poketype()}')
                print(f'{pokemon_2}  {pokemon_2.get_speed()}')
                print('')
 
                self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon
                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon

                if pokemon_1.speed > pokemon_2.speed:
                    if pokemon_2.health > 0:
                        print('hi')
                        print(pokemon_1.health)
                        print(pokemon_2.health)
                        pokemon_2.defend(pokemon_1.attack(pokemon_2))
                        print(pokemon_1.health)
                        print(pokemon_2.health)
                        if pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            

                            if self.check_winner() == None:
                                pokemon_2 = self.trainer_2.get_team().team.pop()
                                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
                            elif self.check_winner() != None:
                                winner = self.check_winner()
                                
                                return winner
                            
                        elif pokemon_2.health > 0: 
                            pokemon_1.defend(pokemon_2.attack(pokemon_1))


                            if pokemon_1.health <= 0:
                                pokemon_2.level_up()

                                if self.check_winner() == None:
                                    pokemon_1 = self.trainer_1.get_team().team.pop()
                                    self.trainer_2.register_pokemon(pokemon_1)
                                else:
                                    winner = self.check_winner()
                                    return winner
                                
                            elif pokemon_1.health > 0 and pokemon_2.health > 0:
                                

                                pokemon_2.health = pokemon_2.get_health() - 1
                                pokemon_1.health = pokemon_1.get_health() - 1

                                if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                    pokemon_1.level_up()
                                    
                                    if self.check_winner() == None:
                                        pokemon_2 = self.trainer_2.get_team().team.pop()
                                        self.trainer_1.register_pokemon(pokemon_2)
                                    else:
                                        winner = self.check_winner()
                                        return winner
                                    
                                elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                    pokemon_2.level_up()

                                    if self.check_winner() == None:
                                        pokemon_1 = self.trainer_1.get_team().team.pop()
                                        self.trainer_2.register_pokemon(pokemon_1)
                                    else:
                                        winner = self.check_winner()
                                        return winner
                                
                    
                    

                elif pokemon_1.speed < pokemon_2.speed:
                    if pokemon_1.health > 0:
                        pokemon_1.defend(pokemon_2.attack(pokemon_1))

                        if pokemon_1.health <= 0:
                            pokemon_2.level_up()

                            if self.check_winner() == None:
                                pokemon_1 = self.trainer_1.get_team().team.pop()
                                self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon
                            elif self.check_winner() != None:
                                winner = self.check_winner()
                                return winner
                            
                        elif pokemon_1.health > 0:
                            pokemon_2.defend(pokemon_1.attack(pokemon_2))

                            if pokemon_2.health <= 0:
                                pokemon_1.level_up()

                                if self.check_winner() == None:
                                    pokemon_2 = self.trainer_2.get_team().team.pop()
                                    self.trainer_1.register_pokemon(pokemon_2)
                                elif self.check_winner() != None:
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
                                        winner = self.check_winner()
                                        return winner
                                    
                                elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                    pokemon_2.level_up()

                                    if self.check_winner() == None:
                                        pokemon_1 = self.trainer_1.get_team().team.pop()
                                        self.trainer_2.register_pokemon(pokemon_1)
                                    elif self.check_winner() != None:
                                        winner = self.check_winner()
                                        return winner
                                    
                elif pokemon_1.speed == pokemon_2.speed:
                    
                    # first attack is here 
                    pokemon_1.defend(pokemon_2.attack(pokemon_1))
                    pokemon_2.defend(pokemon_1.attack(pokemon_2))

                    # second attack is here which one of the pokemon is faint

                    if pokemon_1.health > 0 and pokemon_2.health > 0:
                        pokemon_1.health = pokemon_1.get_health() - 1
                        pokemon_2.health = pokemon_2.get_health() - 1
                        # send back to their team
                        if pokemon_1.health > 0 and pokemon_2.health <= 0:
                            pokemon_1.level_up()
                            if self.check_winner() == None:
                                pokemon_2 = self.trainer_2.get_team().team.pop()
                                self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon
                            elif self.check_winner() != None:
                                winner = self.check_winner()
                                return winner

                            
                            # pokemon 2 should be back
                        elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                            pokemon_2.level_up()
                            if self.check_winner() == None:
                                pokemon_1 = self.trainer_1.get_team().team.pop()
                                self.trainer_2.register_pokemon(pokemon_1)
                            elif self.check_winner() != None:
                                winner = self.check_winner()
                                return winner

                            
                            # pokemon 1 should be back
                        elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
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
                            winner = self.check_winner()
                            return winner
                        
                    elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                        pokemon_2.level_up()

                        if self.check_winner() == None:
                            pokemon_1 = self.trainer_1.get_team().team.pop()
                            self.trainer_2.register_pokemon(pokemon_1)
                        elif self.check_winner() != None:
                            winner = self.check_winner()
                            return winner                        

                    elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                        # nxt battle start 
                        if self.check_winner() == None:
                            pokemon_1 = self.trainer_1.get_team().team.pop()
                            self.trainer_2.register_pokemon(pokemon_1) # here is let the opposite to register the pokemon

                            pokemon_2 = self.trainer_2.get_team().team.pop()
                            self.trainer_1.register_pokemon(pokemon_2) # here is let the opposite to register the pokemon

                        elif self.check_winner() != None:
                            winner = self.check_winner()
                            return winner
                # winner = None

                        
            
    def check_winner(self) -> Trainer | None:
        if len(self.trainer_1.get_team().team) == 0:
            # print(len(self.trainer_2.get_team().team))
            return self.trainer_2
        elif len(self.trainer_2.get_team().team) == 0:
            print(len(self.trainer_1.get_team().team))
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
            self.trainer_2.get_team().assemble_team(self.battle_mode)
        
        elif self.battle_mode.name == "OPTIMISE":
            self.trainer_1.get_team().assemble_team(self.battle_mode)
            self.trainer_2.get_team().assemble_team(self.battle_mode)

    
    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError




if __name__ == '__main__':
    # test 3.1
    random.seed(20)
    t1 = Trainer('Gary')
    t2 = Trainer('Ash')

    b = Battle(t1, t2, BattleMode.SET)
    b._create_teams()
    t1.get_team().special(BattleMode.SET)
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")


