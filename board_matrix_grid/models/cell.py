from ..constants import TILE_KINDS


class Cell:
    """
    Cell contains tiles.

    .. Note:
        A cell may contains multiple tiles so they can be stacked. Like there can be
        a tile for the land type (grass, stone, etc..), another one for decor (tree,
        wall, etc..), then another one for furniture (chest, table, etc..), etc..

        However they would need to be ordered/typed so a land is always at very bottom
        and furniture at the very top.
    """
    def __init__(self, index, row=None, tiles=[]):
        # This represent the cell position in a row, we can also call it a column
        # This may be a weakness since if adding a new cell between other row ones will
        # requires to reindex all further cells
        self.index = index
        self.row = row
        self.tiles = {
            name: None
            for name in TILE_KINDS
        }

        for tile in tiles:
            self.add_tile(tile)

    def __repr__(self):
        return "<{klass}: {index}>".format(
            klass=self.__class__.__name__,
            index=self.index
        )

    def add_tile(self, tile):
        """
        Add a tile to cell.

        This automatically add tile into its kind slot into ``Cell.tiles``.

        We may use instead a dict for tiles with an item for each level (a level
        could store only a single tile). Tile should define its suitable level since
        Tile type should be stored at any level (example: a grass tile is always a
        land, never a decore or furniture).

        Arguments:
            tile (Tile): Tile object to add to cell tiles.

        """
        tile.cell = self
        self.tiles[tile.kind] = tile
