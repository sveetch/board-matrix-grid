class Row:
    """
    Row contains cells
    """
    def __init__(self, index, board=None, cells=[]):
        self.index = index
        self.board = board
        self.cells = []

        for cell in cells:
            self.add_cell(cell)

    def __repr__(self):
        return "<{klass}: {index}>".format(
            klass=self.__class__.__name__,
            index=self.index
        )

    def add_cell(self, cell):
        """
        Add a cell to row.

        Arguments:
            cell (Cell): Cell object to add to row cells.

        """
        cell.row = self
        self.cells.append(cell)
        # Index cell from its current position
        cell.index = len(self.cells) - 1
