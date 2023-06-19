from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_dialog_remote_control import Ui_Dialog_Remote_Control
import sys

from drivers import driver_bluetooth
from widgets import bluetooth_widget


class RemoteCotrolcontrollerDialog(QDialog):

    def __init__(self, parent=None, blt=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Remote_Control()
        self.ui.setupUi(self)
        self.initUi()

        # self.blt = bluetooth_widget.BluetoothWidget("蓝牙")
        self.blt = blt

    def on_stop_clicked(self):
        try:
            self.blt.send_hex_data("0x00")
        except Exception as e:
            print(e)

    def on_forward_clicked(self):
        try:
            self.blt.send_hex_data("0x01")
        except Exception as e:
            print(e)

    def on_backward_clicked(self):
        try:
            self.blt.send_hex_data("0x02")
        except Exception as e:
            print(e)

    def on_left_clicked(self):
        try:
            self.blt.send_hex_data("0x03")
        except Exception as e:
            print(e)

    def on_right_clicked(self):
        try:
            self.blt.send_hex_data("0x04")
        except Exception as e:
            print(e)

    def on_track_clicked(self):
        try:
            self.blt.send_hex_data("0x05")
        except Exception as e:
            print(e)

    def on_surround_clicked(self):
        try:
            self.blt.send_hex_data("0x10")
        except Exception as e:
            print(e)

    def initUi(self):
        self.ui.btn_forward.clicked.connect(self.on_forward_clicked)
        self.ui.btn_backward.clicked.connect(self.on_backward_clicked)
        self.ui.btn_left.clicked.connect(self.on_left_clicked)
        self.ui.btn_right.clicked.connect(self.on_right_clicked)
        self.ui.btn_stop.clicked.connect(self.on_stop_clicked)
        self.ui.btn_surround.clicked.connect(self.on_surround_clicked)
        self.ui.btn_track.clicked.connect(self.on_track_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = RemoteCotrolcontrollerDialog()
    dialog.show()
    sys.exit(app.exec_())
