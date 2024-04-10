from battle import Battle
from battle_mode import BattleMode
from poke_team import Trainer, PokeTeam
from enum import Enum
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple
import random

class BattleTower:
    MIN_LIVES = 1
    MAX_LIVES = 3
    def __init__(self) -> None:
        self.my_trainer = None
        self.lives = None
        self.start = False

    # Hint: use random.randint() for randomisation
    def set_my_trainer(self, trainer: Trainer) -> None:
        '''Sets the player team for the battle tower, and generates between MIN_LIVES and MAX_LIVES lives'''
        self.my_trainer = trainer
        self.lives = random.randint(BattleTower.MIN_LIVES, BattleTower.MAX_LIVES)
        

    def generate_enemy_trainers(self, num_teams: int) -> None:
        '''Randomly generates n enemy teams (n is passed as a parameter). All teams must use selection_mode RANDOM and all battle are fought with battle mode ROTATE. 
        Generate each team a number of lives between MIN_LIVES and MAX_LIVES, after each team is generated but before the next team is generated.'''
        self.enemy_trainers = CircularQueue(num_teams)
        for i in range(num_teams):

            enemy = Trainer("Enemy")
            enemy.pick_team("Random")
            enemy.get_team().assemble_team(BattleMode.ROTATE)
            enemy.enemy_lives = random.randint(BattleTower.MIN_LIVES, BattleTower.MAX_LIVES)
            self.enemy_trainers.append(enemy)
        

    def battles_remaining(self) -> bool:
        ''' Returns True if there are more battles to be had, False if either the player or all enemy teams have ran out of lives.'''

        return self.lives > 0 and len(self.enemy_trainers) > 0
        

    def next_battle(self) -> Tuple[Trainer, Trainer, Trainer, int, int]:
        '''Returns a tuple of the player trainer, the enemy trainer, the winning trainer, the number of lives the player has left, and the number of lives the enemy has left. 
        The winning trainer is the trainer of the team that won the battle. The number of lives should be decremented for the losing team.'''
        self.start = True

        player = self.my_trainer

        enemy = self.enemy_trainers.serve()

        battle = Battle(player, enemy, BattleMode.ROTATE)
        winner = battle.commence_battle()

        # print(winner.get_name())
        # print('im winner team')
        # print(winner.get_team().team)

        if winner.get_name() == player.get_name():
            enemy.enemy_lives -= 1
            if enemy.enemy_lives > 0:
                self.enemy_trainers.append(enemy)

        elif winner.get_name() == enemy.get_name():
            self.lives -= 1
            
        elif winner.get_name() == None:
            self.lives -= 1
            enemy.enemy_lives -= 1
            if enemy.enemy_lives > 0:
                self.enemy_trainers.append(enemy)
        
        
        
        enemy.get_team().regenerate_team(BattleMode.ROTATE)
        
        player.get_team().regenerate_team(BattleMode.ROTATE)
        return (winner, player.get_name(), enemy.get_name(), self.lives, enemy.enemy_lives)
    
    
    def enemies_defeated(self) -> int:
        '''you should keep a counter of the number of enemy lives taken by the player, which this method should return.'''
        total_enemy_lives = 0
        if self.start is False:
            return 0
        else:
            for enemy in self.enemy_trainers.array:
                total_enemy_lives += enemy.enemy_lives
        return total_enemy_lives + self.lives
    


if __name__ == '__main__':
    player_trainer = Trainer('Ash')
    player_trainer.pick_team("Random")
    player_trainer.get_team().assemble_team(BattleMode.ROTATE)
    print(player_trainer.get_team().team)

    bt = BattleTower()
    bt.set_my_trainer(player_trainer)
    print(bt.lives)
    bt.generate_enemy_trainers(2)
    print(len(bt.enemy_trainers))
    print('')
    print(bt.enemies_defeated())
    # team_1 = bt.enemy_trainers.serve()
    # print(team_1.get_team().team)
    # print(team_1.enemy_lives)

    # print('')
    # team_2 = bt.enemy_trainers.serve()
    # print(team_2.get_team().team)
    # print(team_2.enemy_lives)

    player_team = bt.my_trainer
    enemy_team = bt.enemy_trainers.serve()
    print(player_team.get_name())
    print(enemy_team)