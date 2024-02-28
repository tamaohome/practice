# coding: utf-8

class Coordinate(tuple[int, int]):
    """セル座標(row, col)を保持するクラス"""

    def __new__(cls, row: int, col: int):
        return super().__new__(cls, (row, col))

    @property
    def row(self) -> int:
        return self[0]

    @property
    def col(self) -> int:
        return self[1]


if __name__ == "__main__":
    start_pos = Coordinate(4, 1)
    print(start_pos)  # -> (4, 1)
    print(start_pos.row)  # -> 4
    print(start_pos.col)  # -> 1