from typing import Callable
from typing import List, Tuple, Dict
from typing import Literal
from typing import NewType

MODE = Literal['r', 'rb', 'w', 'wb']


def add_two_num(a: int, b: int) -> int:
    return a + b


def test_mul_type(a: int, string: str, f: float, b: bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a": f}
    bl = b
    return list1, tup, d, bl


def open_helper(file: str, mode: MODE) -> str:
    line = ''
    with open(file=file, mode=mode) as f:
        line = f.readline()
    return line


def apply(fn: Callable[[int, int], int], *args: int) -> int:
    return fn(args[0], args[1])


if __name__ == '__main__':
    # 新增类型
    UserId = NewType('UserId', int)
    ProUserId = NewType('ProUserId', UserId)

    open_helper(r'F:\Learning\LearningCode\Learn_Python\country_data.xml', 'r')  # 正确
    # open_helper(r'F:\Learning\LearningCode\Learn_Python\country_data.xml', 'typo')  # pyright 报错

    print(test_mul_type(5, "hhhh", 2.3, False))
