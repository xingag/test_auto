import threading
from time import sleep


class Singleton(object):
    """
    实例化一个对象
    """

    # 锁
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


def task(arg):
    """
    任务
    :param arg:
    :return:
    """
    instance = Singleton()
    print(id(instance), '\n')


if __name__ == '__main__':
    # 3个线程
    for i in range(3):
        t = threading.Thread(target=task, args=[i, ])
        t.start()
