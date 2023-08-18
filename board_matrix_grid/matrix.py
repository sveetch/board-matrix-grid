class Matrix:
    """
    DEPRECATED

    Grid matrix builder.

    Arguments:
        width (integer):
        height (integer):
    """
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows

    def grid(self):
        grid = []

        for y in range(1, self.rows + 1):
            grid.append([
                []
                for x in range(1, self.cols + 1)
            ])

        return grid
