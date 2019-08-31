from copy import copy


class Cell:
    v_line = None  # type: list[Cell]
    h_line = None  # type: list[Cell]
    b_cell = None  # type: list[Cell]
    available_state = None  # type: set[int]
    __state = None  # type: int

    def __init__(self, state=0):
        self.available_state = set(range(1, 10))
        self.__state = state
        if state:
            self.available_state = {state}

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
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
        else:
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
                raise Exception()

    def __str__(self):
        return self.state

    def __repr__(self):
        return str(self.state)

