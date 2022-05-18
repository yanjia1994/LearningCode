# 全局变量
g1 = 1
g2 = []
g3 = []


def f1():
    g1 = 2
    g2.append(1)
    g3 = [1]


f1()
print(g1, g2, g3)

g1 = 1
g2 = []
g3 = []


def f2():
    global g1
    global g2
    global g3

    g1 = 2
    g2.append(1)
    g3 = [1, 2]


f2()
print(g1, g2, g3)

a = [1, 2]
b = a
a = [3, 4]
print(a, b)
print(a, b)
c = (1, 2)
d = c
c = (3, 4)
print(c, d)

list_tuple = ([1, 2], 0)
print("The value of list tuple is", list_tuple)
print("The id of list tuple is", id(list_tuple[0]))

list_tuple[0][0] = 2
print("The value of list tuple is", list_tuple)
print("The id of list tuple is", id(list_tuple[0]))

list_set = {1, 1.0}
print(list_set)


class People:
    a = 0
    b = 0

    def __init__(self) -> None:
        pass

    @classmethod
    def run(cls):
        pass


print(People.__dict__)
