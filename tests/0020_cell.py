from board_matrix_grid.models import (
    BoardMatrix, Row, Cell, Tile,
)


def test_model_cell():
    """
    Cell object
    """
    col = Cell(42)

    assert str(col) == "<Cell: 42>"
    assert repr(col) == "<Cell: 42>"


def test_model_cell_tiles():
    """
    Filling a Cell with Tile objects
    """
    tile_grass = Tile("land", "Grass land")
    tile_sand = Tile("land", "Sand land")
    tile_tree = Tile("decor", "Tree decor")
    tile_stone = Tile("decor", "Stone decor")
    tile_chest = Tile("furniture", "Chest furniture")

    # Add some tiles from arguments
    col_42 = Cell(42, tiles=[tile_grass, tile_stone])
    col_99 = Cell(99, tiles=[tile_sand])

    # Expected tiles
    assert col_42.tiles["land"].value == "Grass land"
    assert col_42.tiles["land"].cell == col_42
    assert col_42.tiles["decor"].value == "Stone decor"
    assert col_42.tiles["decor"].cell == col_42
    assert col_42.tiles["furniture"] == None

    # Add some other tiles from method
    col_42.add_tile(tile_sand)
    col_42.add_tile(tile_chest)

    # Land kind is overwritten
    assert col_42.tiles["land"].value == "Sand land"
    assert col_42.tiles["land"].cell == col_42
    # Decor is left untouched
    assert col_42.tiles["decor"].value == "Stone decor"
    assert col_42.tiles["decor"].cell == col_42
    # Furniture has been added and its tile cell has been changed
    assert col_42.tiles["furniture"].value == "Chest furniture"
    assert col_42.tiles["furniture"].cell == col_42
