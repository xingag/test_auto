from time import sleep

from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.keyboard import send_keys


class WeiXin(object):

    def __init__(self):
        # 获取微信客户端连接应用对象
        self.app = Application(backend='uia').connect(path="D:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

        # 通过title及ClassName获取窗体对象
        self.weixin_pc_window = self.app.window(title=u"微信", class_name="WeChatMainWndForPC")
        self.weixin_pc_window.set_focus()

    def __get_element_postion(self, element):
        """获取元素的中心点位置"""
        # 元素坐标
        element_position = element.rectangle()
        # 算出中心点位置
        center_position = (int((element_position.left + element_position.right) / 2),
                           int((element_position.top + element_position.bottom) / 2))
        return center_position

    def start(self):
        # 1、获取左侧【聊天】切换元素
        chat_list_element = self.weixin_pc_window.child_window(title="聊天", control_type="Button")
        # 2、点击进入到聊天列表
        mouse.click(button='left',
                    coords=self.__get_element_postion(chat_list_element))
        # 3、点击【文件传输助手】进入到聊天页面
        file_helper_element = self.weixin_pc_window.child_window(title="文件传输助手", control_type="ListItem")
        mouse.click(button='left',
                    coords=self.__get_element_postion(file_helper_element))
        # 4、获取输入框元素，模拟输入
        edit_element = self.weixin_pc_window.child_window(title=r"输入", control_type="Edit")
        sleep(2)
        # 输入内容
        edit_element.type_keys("星安果")
        # 使用键盘模拟回车，即：发送
        send_keys('{ENTER}')

        # 5、释放资源
        self.teardown()

    def teardown(self):
        """释放资源"""
        # 结束进程，释放资源
        self.app.kill()


if __name__ == '__main__':
    weixin = WeiXin()
    weixin.start()
