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


def test_model_row_cells():
    """
    Filling a Row with Cell objects
    """
    cell_10 = Cell(10)
    cell_20 = Cell(20)
    cell_30 = Cell(30)
    cell_42 = Cell(42)

    row = Row(1, cells=[cell_42, cell_20])

    assert len(row.cells) == 2

    # Expected tiles
    assert row.cells[0].index == 0

    # TODO: to finish
    assert 1 == 42
