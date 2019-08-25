from cell import Cell


class Field:
    cells = None

    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(Cell())

    def set_cell_state(self, i, j, state):
        self.cells[i][j].state = state
