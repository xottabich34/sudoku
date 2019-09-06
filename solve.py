from copy import copy
from pprint import pprint

from field import Field


def solve(field):
    """

    :param Field field:
    :return:
    """
    if not field.is_sloved():
        i, j = field.get_empty()
        for state in field.cells[i][j].available_state:
            new_field = copy(field)
            new_field.cells[i][j].state = state
            yield from solve(new_field)

    else:
        yield field


def main():
    field = Field()
    with open('in.txt') as f:
        for i in range(9):
            line = f.readline().split()
            for j in range(9):
                state = int(line[j])
                if state:
                    field.set_cell_state(i, j, state)
                    # pprint(field.cells)
    if field.is_sloved():
        pprint(field.cells)
    else:
        all_solutions = set(solve(field))
        for solution in all_solutions:
            pprint(solution.cells)
        pprint(len(all_solutions))


if __name__ == '__main__':
    main()
