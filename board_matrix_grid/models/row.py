class Row:
    """
    Row contains cells
    """
    def __init__(self, index, board=None, cells=[]):
        self.index = index
        self.board = board
        self.cells = cells

    def __repr__(self):
        return "<{klass}: {index}>".format(
            klass=self.__class__.__name__,
            index=self.index
        )
