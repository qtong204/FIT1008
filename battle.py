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
        raise NotImplementedError

    def _create_teams(self) -> Tuple[PokeTeam, PokeTeam]:
        """which turns the PokeTeams from the two trainers into appropriate data structures based on the mode supplied to the battle as an initial argument."""

        team_1 = self.trainer_1.pick_team("random")
        team_2 = self.trainer_2.pick_team("random")

        # if self.battle_mode == BattleMode.SET:
        #     team_1.set_active_pokemon(0)
        #     team_2.set_active_pokemon(0)
        # elif self.battle_mode == BattleMode.ROTATE:
        #     team_1.set_active_pokemon(0)
            # team_2.set_active_pokemon(0)
        #     team_1.set_rotation_order()
        #     team_2.set_rotation_order()
        # elif self.battle_mode == BattleMode.OPTIMIZE:
        #     team_1.set_active_pokemon(0)
        #     team_2.set_active_pokemon(0)
        #     team_1.optimize_team()
        #     team_2.optimize_team()

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

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")

