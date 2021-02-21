from enum import auto

class Params:
    HUMAN_ID = auto()
    MACHINE_ID = auto()
    EMPTY_ID = auto()

class State:
    GAME = auto()
    MACHINE_WIN = auto()
    HUMAN_WIN = auto()
    DRAW = auto()

