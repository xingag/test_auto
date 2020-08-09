def singleton(cls):
    """
    定义单例的装饰器（闭包）
    :param cls:
    :return:
    """
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class Singleton(object):
    """单例实例"""

    def __init__(self, arg1):
        self.arg1 = arg1


if __name__ == '__main__':
    instance1 = Singleton("xag")
    instance2 = Singleton("xingag")

    print(id(instance1))
    print(id(instance2))


