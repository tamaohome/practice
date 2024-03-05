# coding: utf-8


def sum(i, total=0):
    if i == 0:
        return total
    else:
        return sum(i-1, total+i)

# sum()をyield fromで書き換えた関数
def sum2(i, total=0):
    if i == 0:
        yield total
    else:
        yield from sum2(i-1, total+i)


if __name__ == '__main__':
    print("総和の計算:", sum2(10))
    
    