"""
.. Note::
    These classes could be excellent candidates for '__slot__' usage for performance
    improvements, see:

    https://stackoverflow.com/a/28059785

    TL;DR: Hint, __slot__ usage may be hard to manage with class inheritances, so they
    should be avoided if possible (at least Row and Cell should not need about it).

"""
from board_matrix_grid.exceptions import DummyError


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
