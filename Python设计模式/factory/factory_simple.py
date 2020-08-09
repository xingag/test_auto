# 1、简单工厂

from factory.fruit import Banana, Apple, Orange


class FactorySimple(object):
    """简单工厂模式"""

    @staticmethod
    def get_fruit(fruit_name):
        if 'a' == fruit_name:
            return Apple()
        elif 'b' == fruit_name:
            return Banana()
        elif 'o' == fruit_name:
            return Orange()
        else:
            return '没有这种水果'


if __name__ == '__main__':
    # 分别获取3种水果
    # 输入参数，通过简单工厂，返回对应的实例
    instance_apple = FactorySimple.get_fruit('a')
    instance_banana = FactorySimple.get_fruit('b')
    instance_orange = FactorySimple.get_fruit('o')

    print(instance_apple)
    print(instance_banana)
    print(instance_orange)

