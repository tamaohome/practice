# coding: utf-8

"""
list型を継承したクラスを作成する

参考URL: https://kunai-lab.hatenablog.jp/entry/2017/10/19/213134
"""


class StrList(list):
    """要素を文字列型として格納するリスト"""

    def __init__(self, *args):
        super().__init__([self._str(args) for args in args])

    def _str(self, arg):
        """
        - 要素をstr型に変換して返す
        - 要素が配列の場合は再帰的に変換
        - 要素がNoneの場合は空文字に変換
        """
        if isinstance(arg, list):
            return [self._str(item) for item in arg]
        elif arg is None:
            return ""
        else:
            return str(arg)

    def append(self, arg):
        """
        - list.append()のオーバーライド
        - append()で追加される要素をstr型に変換
        """
        super(StrList, self).append(self._str(arg))

    def extend(self, iterable):
        """
        - list.extend()のオーバーライド
        - extend()で追加される要素をstr型に変換
        """
        super(StrList, self).extend([self._str(item) for item in iterable])


if __name__ == "__main__":
    # 格納テスト
    nums = [-1, 0.50, 2**-4, None]
    str_list = StrList(0, 1, [2, nums])
    print(str_list)

    # listメソッドのテスト
    str_list.append(bin(10))
    print(str_list)

    # スライスのテスト
    print(str_list[2:])

    # 長さのテスト
    print(f"配列の長さ: {len(str_list)}")
