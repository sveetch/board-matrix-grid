class BoardMatrix:
    """
    Board contains rows, cells and tiles
    """
    def __init__(self, key, rows=[], cells=[]):
        self.key = key
        self.rows = rows
        self.cells = cells

    def __repr__(self):
        return "<{klass}: {key}>".format(
            klass=self.__class__.__name__,
            key=self.key
        )
