import threading

from PyQt5.QtWidgets import *
from widgets import bluetooth_widget

import sys

from ui.Ui_main_window import Ui_MainWindow


class ToolBoxMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 创建BluetoothWidget类的对象
        self.blt_widget = bluetooth_widget.BluetoothWidget("蓝牙")

        self.init_ui()

    def init_ui(self):
        # 把bluetooth_widget绑定到tab中
        self.ui.tabWidget.addTab(self.blt_widget, "蓝牙调试工具")
        # 开一个子线程执行bluetooth中的scan_devices
        # sub_thread = threading.Thread(target=driver_bluetooth.scan_devices)
        # 开一个子线程执行bluetooth_widget中的get_devices
        sub_thread = threading.Thread(target=self.blt_widget.get_devices)

        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = ToolBoxMainWindow()
    window.show()

    sys.exit(app.exec_())
