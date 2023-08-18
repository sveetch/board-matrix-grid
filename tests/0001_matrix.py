import json
import pytest

from board_matrix_grid.matrix import Matrix


@pytest.mark.skip
def test_matrix():
    """
    DEPRECATED R&D
    """
    matrix = Matrix(3, 4)


    print(json.dumps(matrix.grid(), indent=4))

    assert matrix.grid() == [
        [
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            []
        ]
    ]
