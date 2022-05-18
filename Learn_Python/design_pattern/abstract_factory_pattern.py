from abc import abstractmethod


# 内容：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类类负责创建产品类的实例.
# 角色：
#    Product：抽象产品
#    ConcreteProduct：具体产品
#    Factory：抽象工厂
#    ConcreteFactory：具体工厂
# 缺点：
#     1. 具体产品与具体工厂需要成对添加


# @ 抽象产品
class Payment():
    @abstractmethod
    def pay(self, money):
        pass


# @ 具体产品
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


# @ 抽象工厂
class PaymentFactory():
    @abstractmethod
    def create_payment(self):
        pass


# @ 具体工厂
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


# @ 客户端
if __name__ == "__main__":
    pay_factory = HuabeiFactory()
    pay_tool = pay_factory.create_payment()
    pay_tool.pay(1000)
