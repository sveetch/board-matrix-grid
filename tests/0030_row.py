from board_matrix_grid.models import (
    BoardMatrix, Row, Cell, Tile,
)


def test_model_row():
    """
    Row object
    """
    row = Row(42)

    assert str(row) == "<Row: 42>"
    assert repr(row) == "<Row: 42>"
