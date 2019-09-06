from copy import copy
from typing import List, Set

from exceptions import NoValuesAvailable, TooManyValues


class Cell:

    def __init__(self, state: int = 0):
        self.available_state: Set[int] = set(range(1, 10))
        self.__state: int = state
        if state:
            self.available_state = {state}
        self.v_line: List[Cell] = []
        self.h_line: List[Cell] = []
        self.b_cell: List[Cell] = []

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: int):
        self.available_state = {state}
        self.__state = state
        for cell in self.v_line:
            if not cell.state:
                cell.discard(state)
        for cell in self.h_line:
            if not cell.state:
                cell.discard(state)
        for cell in self.b_cell:
            if not cell.state:
                cell.discard(state)

    def discard(self, state):
        self.available_state.discard(state)
        if len(self.available_state) == 1:
            self.state = self.available_state.pop()
        elif len(self.available_state) > 1:
            a_s = copy(self.available_state)
            for cell in self.v_line:
                a_s.difference_update(cell.available_state)
            for cell in self.h_line:
                a_s.difference_update(cell.available_state)
            for cell in self.b_cell:
                a_s.difference_update(cell.available_state)
            if len(a_s) == 1:
                self.state = a_s.pop()
            elif len(a_s) > 1:
                raise TooManyValues()
        else:
            raise NoValuesAvailable()

    def __str__(self):
        return self.state

    def __repr__(self):
        return str(self.state)

    def __bool__(self):
        return bool(self.__state)

    def __eq__(self, other):
        return self.state==self.state

    def __hash__(self):
        return hash(self.state)
