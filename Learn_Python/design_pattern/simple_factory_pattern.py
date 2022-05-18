from abc import abstractmethod


# 内容：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类类负责创建产品类的实例.
# 角色：
#     Product：抽象产品,是所创建的所有对象的父类，负责描述所有实例所共有的公共接口.
#     Concrete Product：具体产品,是创建目标，所有创建的对象都充当这个角色的某个具体类的实例.
#     Factory：工厂,负责实现创建所有实例的内部逻辑.
# 缺点：
#     1. 违反了开闭原则


# @抽象产品
class Payment():
    @abstractmethod
    def pay(self, money):
        pass


# @具体产品
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


# @工厂
class PaymentFactory():
    def create_payment(slef, pay_type):
        if pay_type == "支付宝":
            return Alipay()
        if pay_type == "花呗":
            return Alipay(True)
        if pay_type == "微信":
            return WechatPay()


# @ 客户端
if __name__ == "__main__":
    pay_factory = PaymentFactory()
    pay_tool = pay_factory.create_payment("花呗")
    pay_tool.pay(10000)
