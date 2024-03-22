# coding: utf-8

from configparser import ConfigParser
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Position:
    def __init__(self, x: str | int = 0, y: str | int = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value: str | int):
        self._x = str(value)

    @y.setter
    def y(self, value: str | int):
        self._y = str(value)


@dataclass
class Size:
    def __init__(self, width: str | int = 0, height: str | int = 0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value: str | int):
        self._width = str(value)

    @height.setter
    def height(self, value: str | int):
        self._height = str(value)


class WindowConfigManager(ConfigParser):
    position = Position()
    size = Size()

    def __init__(self, conf_file: Path | None = None):
        super().__init__()
        self.conf_file = self.file_parser(conf_file)

        if self.conf_file.exists():
            self.read(self.conf_file)
            self.position.x = self.get("Window Size", "x")
            self.position.y = self.get("Window Size", "y")
            self.size.width = self.get("Window Size", "width")
            self.size.height = self.get("Window Size", "height")

    def file_parser(self, path: Path | None = None) -> Path:
        if path:
            return path
        else:
            return Path(__file__).with_suffix(".ini")

    def save_file(self) -> None:
        with self.conf_file.open("w") as f:
            self.write(f)


if __name__ == "__main__":
    config = WindowConfigManager()

    position = Position(150, 200)
    size = Size(800, 600)

    print("ウインドウの位置:", position)
    print("ウインドウのサイズ:", size)
    print(f"上記の設定を [{config.conf_file.name}] に保存します。")

    config.save_file()

    print("iniファイルを以下の通り保存しました。")
    print(config.conf_file.read_text())
