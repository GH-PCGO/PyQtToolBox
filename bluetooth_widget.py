import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from drivers import driver_bluetooth
from ui.Ui_widget_bluetooth import Ui_BluetoothWidget


class BluetoothWidget(QWidget):

    def __init__(self, title):
        super().__init__()
        self.devices = None
        self.ui = Ui_BluetoothWidget()
        self.ui.setupUi(self)
        self.setWindowTitle(title)

        self.device = []

        self.init_ui()
        # 模拟数据
        # self.ui.comboBox_device.addItem("PCPC (B7:7B:1A:07:10:0B)")

    # def on_refresh_clicked(self):
    #     # 存储设备列表
    #     device_list = []
    #     # 开一个子线程执行bluetooth中的scan_devices
    #     sub_thread = threading.Thread(target=driver_bluetooth.scan_devices, args=([device_list],))
    #     # 设置守护主线程
    #     sub_thread.setDaemon(True)
    #     # 启动子线程
    #     sub_thread.start()
    #     # 打印device_list
    #     print(device_list)
    def get_devices(self):
        self.devices = driver_bluetooth.scan_devices()
        # 打印device_list
        # print("Found device:", name, "(", addr, ")")
        # 遍历device_list
        for device in self.devices:
            # print(type(device))
            print(f"设备名：{device[1]} \t设备地址：{device[0]}\r\n")
            self.ui.comboBox_device.addItem(device[1])

    def on_refresh_clicked(self):
        """
        刷新蓝牙设备
        :return:
        """
        # 存储设备列表
        # 开一个子线程执行bluetooth中的scan_devices
        sub_thread = threading.Thread(target=self.get_devices)
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()

    def on_connect_clicked(self):
        print("connecting...")
        # 根据设备名找到目标设备地址
        blt_name = self.ui.comboBox_device.currentText()
        for device in self.devices:
            # 如果设备名匹配，就打印设备地址并退出循环
            if device[1] == self.ui.comboBox_device.currentText():
                blt_address = device[0]
                break
        blt = driver_bluetooth.BluetoothDataTransfer(blt_address, blt_name, 1)
        try:
            sub_thread = threading.Thread(target=blt.connect())

            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()

            # cur_device = self.ui.comboBox_device.currentText()
            # # self.statusBar().showMessage("连接到：{}".format(cur_device))
            # print("连接到：{}".format(cur_device))
        except Exception as e:
            """
            TODO    弹窗提示或者状态栏提示
            """
            print("连接失败", e)

    def on_clr_rev_clicked(self):
        print("clr rev...")

    def on_clr_send_clicked(self):
        # 点击清空发送框的数据
        self.ui.edit_send.clear()
        print("clr send...")

    def on_send_clicked(self):
        send_msg = self.ui.edit_send.toPlainText()
        print(send_msg)

    def run_scanner(self):
        pass

    def init_ui(self):
        # 给刷新按钮绑定事件
        self.ui.btn_refresh.clicked.connect(self.on_refresh_clicked)
        # 给连接按钮绑定事件
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        # 给清空接收区按钮绑定事件
        self.ui.btn_clr_rev.clicked.connect(self.on_clr_rev_clicked)
        self.ui.btn_clr_send.clicked.connect(self.on_clr_send_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     window = BluetoothWidget("蓝牙调试工具")
#     window.show()
#
#     sys.exit(app.exec_())