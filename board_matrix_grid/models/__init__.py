"""
Board matrix models.

.. Warning::
    Model objets maintain a circular references between them (Cell contains tiles that
    store their related Cell object). So they are not safe for a naive recursive
    digging, like a JSON dump may fail because of circular references.

.. Note::
    These classes could be excellent candidates for '__slot__' usage for performance
    improvements, see:

    https://stackoverflow.com/a/28059785

    TL;DR: Hint, __slot__ usage may be hard to manage with class inheritances, so they
    should be avoided if possible (at least Row and Cell should not need about it).

"""
from .board import BoardMatrix
from .cell import Cell
from .row import Row
from .tile import Tile


__all__ = [
    "BoardMatrix",
    "Cell",
    "Row",
    "Tile",
]
