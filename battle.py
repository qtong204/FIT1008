from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode


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
        if self.battle_mode.name == "SET":
            pokemon_1 = self.trainer_1.get_team().pop()
            pokemon_2 = self.trainer_2.get_team().pop()
            # one alive one dead 
            while winner == None:
                if self.trainer_1.get_team().is_empty() or self.trainer_2.get_team().is_empty():
                    # will stop the battle and return the winner
                    if self.trainer_1.get_team().is_empty():
                        winner = self.trainer_2
                        return winner
                    elif self.trainer_2.get_team().is_empty():
                        winner = self.trainer_1
                        return winner            
                    
                    
                elif pokemon_1.speed > pokemon_2.speed:
                    # pokemon_1.attack(pokemon_2)
                    pokemon_2.defend(pokemon_1.attack(pokemon_2))
                    # should here be add on the defence
                    if pokemon_2.health < 0:
                        self.trainer_2.get_team().pop()
                        pokemon_1.level_up()
                    
                        return winner == None
                    

                elif pokemon_1.speed < pokemon_2.speed:
                    pokemon_2.attack(pokemon_1)
                    pokemon_1.defend(pokemon_2.attack(pokemon_1))

                    if pokemon_1.health < 0:
                        self.trainer_1.get_team().pop()
                        pokemon_2.level_up()

                        return winner == None
                    
                
                elif pokemon_1.speed == pokemon_2.speed:
                    
                    # first attack is here 
                    pokemon_1.attack(pokemon_2)
                    pokemon_2.attack(pokemon_1)
                    # second attack is here which one of the pokemon is faint

                    if pokemon_1.health > 0 and pokemon_2.health > 0:
                        pokemon_1.attack(pokemon_2)
                        pokemon_2.attack(pokemon_1)
                        if pokemon_1.health > 0 and pokemon_2.health > 0:
                            pokemon_1.health = pokemon_1.get_health() - 1
                            pokemon_2.health = pokemon_2.get_health() - 1
                            # send back to their team
                            if pokemon_1.health > 0 and pokemon_2.health <= 0:
                                pokemon_1.level_up()
                                self.trainer_2.get_team().pop()
                                return winner == None
                                # pokemon 2 should be back
                            elif pokemon_1.health <= 0 and pokemon_2.health > 0:
                                pokemon_2.level_up()
                                self.trainer_1.get_team().pop()
                                return winner == None
                                # pokemon 1 should be back
                            elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                                return winner == None # depend on the health and the battle mode, this battle should be fight until the pokemon faint

                            
                    
                    elif pokemon_1.health > 0 or pokemon_2.health > 0:
                        # second_attack
                        if pokemon_1.health > 0:
                            pokemon_2.defend(pokemon_1.attack(pokemon_2))
                            if pokemon_2.health <= 0:
                                pokemon_1.level_up()
                                self.trainer_2.get_team().pop()
                                return winner == None
                            
                                # pokemon 2 should be back
                        elif pokemon_2.health > 0:
                            pokemon_1.defend(pokemon_2.attack(pokemon_1))
                            if pokemon_1.health <= 0:
                                pokemon_2.level_up()
                                self.trainer_1.get_team().pop()
                                # pokemon 1 should be back


                            # here should pop the second pokemon from the team else i call back to the team
                        

                    elif pokemon_1.health <= 0 and pokemon_2.health <= 0:
                        # nxt battle start 
                        self.trainer_1.get_team().pop()
                        self.trainer_2.get_team().pop()
                        return winner == None




        
            

        
        

    def _create_teams(self) -> Tuple[PokeTeam, PokeTeam]:
        """which turns the PokeTeams from the two trainers into appropriate data structures based on the mode supplied to the battle as an initial argument."""

        team_1 = self.trainer_1.pick_team("random")
        # team_1.assemble_team(self.battle_mode)

        
        team_2 = self.trainer_2.pick_team("random")

        # team_1.assemble_team(self.battle_mode)
        # team_2.assemble_team(self.battle_mode)

        # team_2.assemble_team(self.battle_mode)



        return team_1, team_2
    
    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError





if __name__ == '__main__':
    t1 = Trainer('Ash')
    t1.pick_team("random")

    t2 = Trainer('Gary')
    t2.pick_team('random')
    b = Battle(t1, t2, BattleMode.ROTATE)
    winner = b.commence_battle()
    print(b._create_teams())
    

    # if winner is None:
    #     print("Its a draw")
    # else:
    #     print(f"The winner is {winner.get_name()}")

