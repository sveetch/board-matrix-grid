from board_matrix_grid.models import (
    BoardMatrix, Row, Cell, Tile,
)


def test_model_tile():
    """
    Tile object
    """
    tile = Tile("land", "A grass plot")

    assert str(tile) == "A grass plot"
    assert repr(tile) == "<Tile: A grass plot>"
