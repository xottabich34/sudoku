import pprint
from copy import deepcopy
from typing import List

from cell import Cell


class Field:
    cells = None  # type: List[List[Cell]]

    def __init__(self, cells=None):
        """
        :param List[List[Cell]] cells:
        """
        if not cells:
            self.cells = []
            for i in range(9):
                self.cells.append([])
                for j in range(9):
                    self.cells[i].append(Cell())
        else:
            self.cells = cells

        for i in range(9):
            for j in range(9):
                self.cells[i][j].v_line = []
                self.cells[i][j].h_line = []
                self.cells[i][j].b_cell = []
                for i2 in range(9):
                    self.cells[i][j].v_line.append(self.cells[i2][j])
                    self.cells[i][j].h_line.append(self.cells[i][i2])

                for i2 in range(3):
                    for j2 in range(3):
                        self.cells[i][j].b_cell.append(self.cells[int(i / 3) * 3 + i2][int(j / 3) * 3 + j2])

    def set_cell_state(self, i, j, state):
        self.cells[i][j].state = state

    def is_sloved(self):
        return all(x for row in self.cells for x in row)

    def __copy__(self):
        return Field(deepcopy(self.cells))

    def __hash__(self):

        return hash(tuple(tuple(row) for row in self.cells))

    def __eq__(self, other):
        """

        :param Field other:
        :return:
        """
        for rows in zip(self.cells, other.cells):
            if rows[0] != rows[1]:
                return False
        return True

    def get_empty(self):
        for row in range(9):
            for cell in range(9):
                if not self.cells[row][cell]:
                    return row, cell

    def __str__(self):
        return pprint.pformat(self.cells)

    def __iter__(self):
        return iter(self.cells)

    def is_sloved_correctly(self):
        if self.is_sloved():
            for i, j in [(0,0),(3,1),(6,2),(1,3),(4,4),(7,5),(2,6),(5,7),(8,8)]:
                if not len(set(self.cells[i][j].b_cell))==len(set(self.cells[i][j].v_line))==len(set(self.cells[i][j].h_line))==9:
                    return False
            return True
        return False
