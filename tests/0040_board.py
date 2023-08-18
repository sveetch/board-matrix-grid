from board_matrix_grid.models import (
    BoardMatrix, Row, Cell, Tile,
)


def test_model_board():
    """
    BoardMatrix object
    """
    matrix = BoardMatrix("Hello")

    assert str(matrix) == "<BoardMatrix: Hello>"
    assert repr(matrix) == "<BoardMatrix: Hello>"
