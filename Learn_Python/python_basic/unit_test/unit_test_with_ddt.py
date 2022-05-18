
import unittest

from ddt import ddt, data, unpack, file_data


@ddt
class MyDdtTest(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
        return super().setUpClass()

    # 类的释放
    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")
        return super().tearDownClass()

    # 测试用例的初始化
    def setUp(self) -> None:
        print("set up")
        return super().setUp()

    # 测试用例的释放
    def tearDown(self) -> None:
        print("tear down")
        return super().tearDown()

    # 自定义函数
    def add(self, num1, num2):
        return num1 + num2

    # 测试用例1
    @data(1, 2, 3)
    def test_1(self, num):
        print("num =", num)

    # 测试用例2
    @data((1, 2), (3, 4))
    @unpack
    def test_2(self, num1, num2):
        print("num1 =", num1, end=", ")
        print("num2 =", num2, end=", ")
        print("num1 + num2 =", self.add(num1, num2), end="\n")

    # 测试用例3
    @file_data("ddt_data.yml")
    def test_3(self, **kwargs):
        print("name =", kwargs["name"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
