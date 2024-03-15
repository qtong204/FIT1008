from enum import Enum

class BattleMode(Enum):
    SET = 0
    ROTATE = 1
    OPTIMISE = 2

print(BattleMode.SET)
print(BattleMode.SET.name)
