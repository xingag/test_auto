# 单例模式
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    # 构建3个实例
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()

    # 打印出实例的内存地址，判断是否是同一个实例
    print(id(instance1))
    print(id(instance2))
    print(id(instance3))
