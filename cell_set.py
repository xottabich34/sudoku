
class CellSet:
    cells = None
    not_used = None
    used = None

    def __init__(self, cells):
        self.cells = []
        for cell in cells:
            self.cells.append(cell)
            if cell:
                pass
