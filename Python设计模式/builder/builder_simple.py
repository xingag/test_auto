# 购买一个车，流程是：准备钱、看车、试驾、购买


# 车
from time import sleep


class Car(object):
    def __init__(self):
        # 准备的钱
        self.money = None

        # 去哪里看车
        self.address = None

        # 试驾什么车
        self.car_name = None

        # 购买时间是
        self.buy_time = None

    def __str__(self):
        return "准备了：%s,去%s看车，试驾了%s,下单了，购买时间是：%s" % (self.money, self.address, self.car_name, self.buy_time)


# 创建者
class CarBuilder(object):
    def __init__(self):
        self.car = Car()

    def ready_money(self, money):
        """
        准备的金额
        :param money:
        :return:
        """
        self.car.money = money
        sleep(0.5)
        return self

    def see_car(self, address):
        """
        去哪里看车
        :param address:
        :return:
        """
        self.car.address = address
        sleep(0.5)
        return self

    def test_drive(self, car_name):
        """
        试驾了什么车
        :param car_name:
        :return:
        """
        self.car.car_name = car_name
        sleep(0.5)
        return self

    def buy_car(self, buy_time):
        """
        下单时间
        :param buy_time:
        :return:
        """
        self.car.buy_time = buy_time
        sleep(0.5)
        return self


# 负责人
class Director(object):
    def __init__(self):
        self.builder = None

    def build(self, builder):
        self.builder = builder
        self.builder. \
            ready_money("100万"). \
            see_car("4S店"). \
            test_drive("奥迪Q7"). \
            buy_car("2020年8月1日")

        # 返回构建的对象
        return self.builder.car


if __name__ == '__main__':
    # 实例化一个构建者对象
    car_builder = CarBuilder()
    # 实例化一个负责人
    director = Director()

    # 构建的对象
    car = director.build(car_builder)

    print(car)
