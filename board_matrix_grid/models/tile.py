from ..constants import TILE_KINDS


class Tile:
    """
    A location in a board to hold its features settings.

    .. Note:
        A same tile can not be shared to many cells since a tile is tied to a single
        cell only. A map build could use a proxy object which would clone a generic
        tile type but always returning a new Tile object (with generic settings).
    """
    def __init__(self, kind, value, cell=None):
        if kind not in TILE_KINDS:
            raise KeyError("Unknow given Tile kind: {}".format(kind))

        self.kind = kind
        self.cell = cell
        self.value = value


    def __repr__(self):
        return "<{klass}: {value}>".format(
            klass=self.__class__.__name__,
            value=self.value
        )

    def __str__(self):
        return self.value
