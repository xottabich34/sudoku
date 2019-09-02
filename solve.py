from pprint import pprint

from field import Field

FIELD = Field()
for i in range(9):
    for j in range(9):
        FIELD.cells[i][j].v_line = []
        FIELD.cells[i][j].h_line = []
        FIELD.cells[i][j].b_cell = []
        for i2 in range(9):
            FIELD.cells[i][j].v_line.append(FIELD.cells[i2][j])
            FIELD.cells[i][j].h_line.append(FIELD.cells[i][i2])

        for i2 in range(3):
            for j2 in range(3):
                i3 = int(i/3)*3 + i2
                # print(f'{i} {j} {i2} {j2} {int(i/3)*3 + i2} {int(j/3)+j2}')
                FIELD.cells[i][j].b_cell.append(FIELD.cells[int(i/3)*3 + i2][int(j/3)*3+j2])


def solve():
    with open('in.txt') as f:
        for i in range(9):
            line = f.readline().split()
            for j in range(9):
                state = int(line[j])
                if state:
                    FIELD.set_cell_state(i, j, state)
                    pprint(FIELD.cells)


if __name__ == '__main__':
    solve()
    pprint(FIELD.cells)
