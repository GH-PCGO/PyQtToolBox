from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from UI.Ui_main_window import Ui_MainWindow


class ToolBoxMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ToolBoxMainWindow()
    window.show()

    sys.exit(app.exec_())
