import os

import yaml

from utils.element_util import *

# 所有设备ID
devices = []


# 代码改进

class ADBControl(object):
    def __init__(self):
        with open('./../steps_adb.yaml', 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        self.packageName = data.get('package_name')
        self.home_activity = data.get('home_activity')

        # 执行步骤
        self.steps = data.get('steps')

    def get_online_devices(self):
        """
        获取所有在线的设备
        :return:
        """
        global devices
        try:
            for device_serias_name in exec_cmd("adb devices"):
                # 过滤掉第一条数据及不在线的设备
                if "device" in device_serias_name:
                    devices.append(device_serias_name.split("\t")[0])
            devices = devices[1:]
        except Exception as e:
            print(e)

        # 连上的所有设备及数量
        return devices

    def start_app(self):
        """
        打开App
        :return: 
        """
        for device in devices:
            os.popen("adb -s " + device + " shell am start -W {}/{}".format(self.packageName, self.home_activity))

        print('等待加载完成...')
        sleep(10)

    def stop_all(self):
        """
        关闭应用
        :return:
        """
        for device in devices:
            os.popen("adb -s " + device + " shell am force-stop  %s" % self.packageName)

    def run_task(self):
        """
        执行步骤
        :param devices:
        :return:
        """
        print(self.steps)

        for step in self.steps:

            for device in devices:

                # 操作名称
                step_name = list(step)[0]

                if step_name == 'save_ui_tree_to_local':
                    # 保存UI数到本地
                    method = step.get(step_name).get('method')
                    save_ui_tree_to_local(device)
                elif step_name == 'find_element_and_click':
                    element_id = step.get(step_name).get('id')
                    # 获取元素的坐标
                    bound_search_input = get_element_position(element_id, device)
                    # 点击元素
                    exec_cmd('adb -s %s shell input tap %s %s' % (device, bound_search_input[0], bound_search_input[1]))
                elif step_name == 'input_content':
                    input_content = step.get(step_name).get('content')
                    # 模拟输入
                    exec_cmd('adb -s %s shell input text %s' % (device, input_content))
                else:
                    print('其他操作步骤')


if __name__ == "__main__":
    adb_control = ADBControl()

    # 1、获取所有设备
    adb_control.get_online_devices()

    adb_control.start_app()

    # 2、执行命令
    adb_control.run_task()

    sleep(5)

    # 3、关闭所有设备上的App
    adb_control.stop_all()
