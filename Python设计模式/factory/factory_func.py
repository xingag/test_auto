# 2、工厂方法
# 目的:扩展的时候，尽量不修改原有代码

import abc
from factory.fruit import *

class AbstractFactory(object):
    """抽象工厂"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_fruit(self):
        pass


class AppleFactory(AbstractFactory):
    """生产苹果"""

    def get_fruit(self):
        return Apple()


class BananaFactory(AbstractFactory):
    """生产香蕉"""

    def get_fruit(self):
        return Banana()


class OrangeFactory(AbstractFactory):
    """生产橘子"""

    def get_fruit(self):
        return Orange()


if __name__ == '__main__':
    # 每个工厂负责生产自己的产品也避免了我们在新增产品时需要修改工厂的代码，而只要增加相应的工厂即可
    instance_apple = AppleFactory().get_fruit()
    instance_banana = BananaFactory().get_fruit()
    instance_orange = OrangeFactory().get_fruit()

    print(instance_apple)
    print(instance_banana)
    print(instance_orange)
