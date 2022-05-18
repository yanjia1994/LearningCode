import unittest


class MyTest(unittest.TestCase):
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
    def test_a(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("test_a is successful")

    # 测试用例2
    def test_b(self):
        num_sum = self.add(1, 2)
        print("num_sum =", num_sum)
        self.assertEqual(num_sum, 3)


if __name__ == '__main__':
    # 添加测试用例到测试套件
    suite = unittest.TestSuite()

    # 方法1：多次调用addTest
    suite.addTest(MyTest("test_b"))
    suite.addTest(MyTest("test_a"))

    # 方法2：批量添加用例，调用addTests
    cases = [MyTest("test_b"), MyTest("test_a")]
    suite.addTests(cases)

    # 方法3：从文件中加载
    # discover = unittest.defaultTestLoader.discover("./", pattern="s*.py")
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    # 运行
    runner = unittest.TextTestRunner()
    runner.run(suite)
