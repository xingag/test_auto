# 3、抽象工厂
import abc


class MaoXW_CC(object):
    """川菜-毛血旺"""

    def __str__(self):
        return "川菜-毛血旺"


class XiaoCR_CC(object):
    """川菜-小炒肉"""

    def __str__(self):
        return "川菜-小炒肉"


class MaoXW_XC(object):
    """湘菜-毛血旺"""

    def __str__(self):
        return "湘菜-毛血旺"


class XiaoCR_XC(object):
    """湘菜-小炒肉"""

    def __str__(self):
        return "湘菜-小炒肉"


class AbstractFactory(object):
    """
    抽象工厂
    既可以生产毛血旺，也可以生成小炒肉
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_maoxw(self):
        pass

    @abc.abstractmethod
    def product_xiaocr(self):
        pass


class CCFactory(AbstractFactory):
    """川菜馆"""

    def product_maoxw(self):
        return MaoXW_CC()

    def product_xiaocr(self):
        return XiaoCR_CC()


class XCFactory(AbstractFactory):
    """湘菜馆"""

    def product_maoxw(self):
        return MaoXW_XC()

    def product_xiaocr(self):
        return XiaoCR_XC()


if __name__ == '__main__':
    # 川菜炒两个菜，分别是：毛血旺和小炒肉
    maoxw_cc = CCFactory().product_maoxw()
    xiaocr_cc = CCFactory().product_xiaocr()

    print(maoxw_cc, xiaocr_cc)

    maoxw_xc = XCFactory().product_maoxw()
    xiaocr_xc = XCFactory().product_xiaocr()

    print(maoxw_xc, xiaocr_xc)
