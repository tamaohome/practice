# coding: utf-8


class Integers:
    def __init__(self, *args):
        self._nums = [int(num) for num in args]

    # integers[1], integers[1:2]の指定がある場合に呼び出される
    # 注意点: indexがNoneの場合は呼び出されないので、integers自体はイテレータとして扱う
    def __getitem__(self, index: int | slice):
        return self._nums[index]

    # integers自体はイテレータとして扱う
    def __iter__(self):
        return iter(self._nums)


if __name__ == "__main__":
    integers = Integers(1, 2, 3, 4, 5)
    print(integers[2])     # -> 3
    print(integers[1:3])   # -> [2, 3]
    print(list(integers))  # -> [1, 2, 3, 4, 5]
