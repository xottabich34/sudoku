from copy import copy, deepcopy
import pprint


def chain_zip(*iterables):
    iterables = list(iterables)
    while iterables:
        gen = iterables.pop(0)
        try:
            yield next(gen)
        except StopIteration:
            continue
        iterables.append(gen)


USED_FRIDGE = set()


class Fridge(object):
    def __init__(self, cols, rows, field=None):
        if field:
            self.field = field
        else:
            self.field = [[True for _ in range(cols)] for _ in range(rows)]
        self.cols = cols
        self.rows = rows

    def press(self, col, row):

        for i in range(self.cols):
            # print(i, row)
            self.field[row][i] = not self.field[row][i]
        for j in range(self.rows):
            self.field[j][col] = not self.field[j][col]
        self.field[row][col] = not self.field[row][col]

    def change(self, col, row):
        self.field[row][col] = not self.field[row][col]

    def __copy__(self):
        return Fridge(self.cols, self.rows, deepcopy(self.field))

    def iswin(self):
        return all(self.field[j][i] for i in range(self.cols) for j in range(self.rows))

    def __eq__(self, other):
        return self.field == other.field

    def __hash__(self):
        res = int(''.join(map(str, map(int, [x for i in self.field for x in i]))), 2)
        return res

    def __repr__(self):
        return pprint.pformat(self.field)

    def all_vars(self):
        """

        :return list[]:
        :rtype: list[list[Fridge]]
        """
        m = []
        for i in range(self.cols):
            m.append([])
            for j in range(self.rows):
                new = copy(self)
                new.press(i, j)
                m[i].append(new)
        return m

    def canbesolved(self, used=None, indent=0):
        if not used:
            used = set()
        if self.iswin():
            yield True
        elif self in used:
            yield False
        else:
            used.add(self)
            yield False
            all_vars = [item.canbesolved(used, indent + 4) for row in self.all_vars() for item in row]
            yield any(chain_zip(*all_vars))


def all_(fridge, col, row):
    """
    генератор всех возможных "холодильников". каждый из переключателей во всех возможных состояниях (True| False)
    количество возвращаемых "холодильников" 2^(n*m)
    :param Fridge fridge:
    :param int col:
    :param int row:
    :return collections.Iterable[Fridge]:
    """
    fridge = copy(fridge)
    fridge_changed = copy(fridge)
    fridge_changed.change(col, row)
    for fr in (fridge, fridge_changed):
        if col == (fr.cols - 1) and row == (fr.rows - 1):
            yield fr
        elif col == (fr.cols - 1):
            yield from all_(fr, 0, row + 1)
        else:
            yield from all_(fr, col + 1, row)


def main():
    for fridge in all_(Fridge(2, 2), 0, 0):
        pprint.pprint(fridge.field)
        pprint.pprint(any(fridge.canbesolved()))


if __name__ == '__main__':
    main()