# coding: utf-8

import sys
from configparser import ConfigParser
from pathlib import Path
from dataclasses import dataclass

# from collections import namedtuple


@dataclass
class Position:
    _min_x, _min_y = 0, 0
    
    def __init__(self, x: str | int = 0, y: str | int = 0):
        self._x = int(x)
        self._y = int(y)
        self.parse_point()

    def parse_point(self) -> None:
        """x, yをmin_point以上に設定"""
        self._x = self._min_x if self._x < self._min_x else self._x
        self._y = self._min_y if self._y < self._min_y else self._y

    @property
    def point(self) -> tuple[int, int]:
        return self._x, self._y
    
    @property
    def min_point(self) -> tuple[int, int]:
        return self._min_x, self._min_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value: str | int):
        self._x = int(value)
        self.parse_point()

    @y.setter
    def y(self, value: str | int):
        self._y = int(value)
        self.parse_point()
    
    @point.setter
    def point(self, value: tuple[str | int, str | int]):
        self._x = int(value[0])
        self._y = int(value[1])
        self.parse_point()
    
    @min_point.setter
    def min_point(self, value: tuple[str | int, str | int]):
        self._x = int(value[0])
        self._y = int(value[1])
        self.parse_point()


@dataclass
class Size:
    _min_width, _min_height = 200, 80

    def __init__(self, width: str | int = 0, height: str | int = 0):
        self._width = int(width)
        self._height = int(height)

    def parse_size(self) -> None:
        """width, heightの最小値を適用"""
        self._width = self._min_width if self._width < self._min_width else self._width
        self._height = self._min_height if self._height < self._min_height else self._height

    @property
    def size(self) -> tuple[int, int]:
        return self._width, self._height

    @property
    def min_size(self) -> tuple[int, int]:
        return self._min_width, self._min_height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @width.setter
    def width(self, value: str | int):
        self._width = int(value)
        self.parse_size()

    @height.setter
    def height(self, value: str | int):
        self._height = int(value)
        self.parse_size()

    @size.setter
    def size(self, value: tuple[str | int, str | int]):
        self._width = int(value[0])
        self._height = int(value[1])
        self.parse_size()

    @min_size.setter
    def min_size(self, value: tuple[str | int, str | int]):
        self._width = int(value[0])
        self._height = int(value[1])
        self.parse_size()


class ConfigManager(ConfigParser):
    position = Position()
    size = Size()

    def __init__(self, ini_file: Path | str):
        super().__init__()
        self.ini_file = self.ini_file_parser(ini_file)

        try:
            self.read(self.ini_file)
            self.position.x = int(self.get("Window Position", "x"))
            self.position.y = int(self.get("Window Position", "y"))
            self.size.width = int(self.get("Window Size", "width"))
            self.size.height = int(self.get("Window Size", "height"))
        except Exception:
            pass

    def read_ini_file(self, ini_file: Path | str) -> None:
        ini_file = self.ini_file_parser(ini_file)
        self.read(ini_file)
        self.position.x = self.get("Window Position", "x")
        self.position.y = self.get("Window Position", "y")
        self.size.width = self.get("Window Size", "width")
        self.size.height = self.get("Window Size", "height")

    def ini_file_parser(self, path: Path | str | None = None) -> Path:
        if isinstance(path, Path):
            return path
        elif isinstance(path, str):
            return Path(path).with_suffix(".ini")
        else:
            raise ValueError("iniファイルのパスを指定してください。")

    def save(self) -> None:
        print("save(): iniファイルに設定を保存します。")
        self["Window Position"] = {
            "x": str(self.position.x),
            "y": str(self.position.y),
        }
        self["Window Size"] = {
            "width": str(self.size.width),
            "height": str(self.size.height),
        }

        with self.ini_file.open("w") as f:
            self.write(f)


# test
if __name__ == "__main__":
    config = ConfigManager(__file__)

    position = Position(150, 200)
    size = Size(800, 600)

    print("ウインドウの位置:", position)
    print("ウインドウのサイズ:", size)
    print(f"上記の設定を [{config.ini_file.name}] に保存します。")

    config.save()

    print("iniファイルを以下の通り保存しました。")
    print(config.ini_file.read_text())
