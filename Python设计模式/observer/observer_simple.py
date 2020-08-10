# 简单的观察者模式


# 观察者
class Observer(object):

    def __init__(self, subject):
        # 初始化观察者，并注册
        subject.register(self)

    def update(self, arg1):
        """获取通知"""
        print('观察者收到监听消息，参数为：', arg1)


# 主体对象（被观察对象）
class Subject(object):

    def __init__(self):
        # 所有的观察者
        self.observers = []
        self.foo = None

    def register(self, observer):
        """添加观察者"""
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('已经存在，添加失败！')

    def unregister(self, observer):
        """注销观察者"""
        try:
            self.observers.remove(observer)
        except ValueError:
            print('注销观察者失败')

    def notify(self):
        """通知所有的观察者"""
        for item in self.observers:
            item.update(self.foo)

    def modify_value(self):
        """
        修改变量的值
        :return:
        """
        self.foo = "公众号：AirPython"

        # 修改后，通知所有观察者
        self.notify()


if __name__ == '__main__':
    # 主体对象
    subject = Subject()
    # 观察者
    observer = Observer(subject)

    # 测试
    subject.modify_value()
