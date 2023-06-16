from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from ui.Ui_main_window import Ui_MainWindow


class ToolBoxMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_ui()

    def on_refresh_clicked(self):
        print("refresh...")

    def on_connect_clicked(self):
        print("connect...")

    def on_clr_rev_clicked(self):
        print("clr rev...")

    def on_clr_send_clicked(self):
        print("clr send...")

    def on_send_clicked(self):
        print("send...")

    def init_ui(self):
        # 给刷新按钮绑定事件
        self.ui.btn_refresh.clicked.connect(self.on_refresh_clicked)
        # 给连接按钮绑定事件
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        # 给清空接收区按钮绑定事件
        self.ui.btn_clr_rev.clicked.connect(self.on_clr_rev_clicked)
        self.ui.btn_clr_send.clicked.connect(self.on_clr_send_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ToolBoxMainWindow()
    window.show()

    sys.exit(app.exec_())
