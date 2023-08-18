from board_matrix_grid.models import (
    BoardMatrix, Row, Cell, Tile,
)


def test_model_cell():
    """
    Cell object
    """
    cell = Cell(42)

    assert str(cell) == "<Cell: 42>"
    assert repr(cell) == "<Cell: 42>"


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
    cell_42 = Cell(42, tiles=[tile_grass, tile_stone])
    cell_99 = Cell(99, tiles=[tile_sand])

    # Expected tiles
    assert cell_42.tiles["land"].value == "Grass land"
    assert cell_42.tiles["land"].cell == cell_42
    assert cell_42.tiles["decor"].value == "Stone decor"
    assert cell_42.tiles["decor"].cell == cell_42
    assert cell_42.tiles["furniture"] == None

    # Add some other tiles from method
    cell_42.add_tile(tile_sand)
    cell_42.add_tile(tile_chest)

    # Land kind is overwritten
    assert cell_42.tiles["land"].value == "Sand land"
    assert cell_42.tiles["land"].cell == cell_42
    # Decor is left untouched
    assert cell_42.tiles["decor"].value == "Stone decor"
    assert cell_42.tiles["decor"].cell == cell_42
    # Furniture has been added and its tile cell has been changed
    assert cell_42.tiles["furniture"].value == "Chest furniture"
    assert cell_42.tiles["furniture"].cell == cell_42
