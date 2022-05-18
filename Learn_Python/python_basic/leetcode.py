class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, name):
        self.name = name


for x in range(3):
    if x > 3:
        print("x =", x)
        break
else:
    print("循环结束，不是break退出。")
