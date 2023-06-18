# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_remote_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Remote_Control(object):
    def setupUi(self, Dialog_Remote_Control):
        Dialog_Remote_Control.setObjectName("Dialog_Remote_Control")
        Dialog_Remote_Control.resize(443, 436)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/remote_control/icon/remote_control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Remote_Control.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog_Remote_Control)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog_Remote_Control)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 0, 1, 2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog_Remote_Control)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 0, 2, 1, 2)
        self.btn_ultrasonic = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_ultrasonic.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_ultrasonic.setObjectName("btn_ultrasonic")
        self.gridLayout_2.addWidget(self.btn_ultrasonic, 1, 0, 2, 1)
        self.btn_surround = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_surround.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_surround.setObjectName("btn_surround")
        self.gridLayout_2.addWidget(self.btn_surround, 1, 1, 2, 1)
        self.btn_track = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_track.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_track.setObjectName("btn_track")
        self.gridLayout_2.addWidget(self.btn_track, 1, 2, 2, 1)
        self.btn_speed_up = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_speed_up.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_speed_up.setObjectName("btn_speed_up")
        self.gridLayout_2.addWidget(self.btn_speed_up, 1, 3, 1, 1)
        self.btn_speed_down = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_speed_down.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_speed_down.setObjectName("btn_speed_down")
        self.gridLayout_2.addWidget(self.btn_speed_down, 2, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_left = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_left.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_left.setObjectName("btn_left")
        self.gridLayout.addWidget(self.btn_left, 1, 0, 1, 1)
        self.btn_right = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_right.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_right.setObjectName("btn_right")
        self.gridLayout.addWidget(self.btn_right, 1, 2, 1, 1)
        self.btn_backward = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_backward.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_backward.setObjectName("btn_backward")
        self.gridLayout.addWidget(self.btn_backward, 2, 1, 1, 1)
        self.btn_forward = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_forward.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_forward.setObjectName("btn_forward")
        self.gridLayout.addWidget(self.btn_forward, 0, 1, 1, 1)
        self.btn_stop = QtWidgets.QPushButton(Dialog_Remote_Control)
        self.btn_stop.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_stop.setText("")
        self.btn_stop.setObjectName("btn_stop")
        self.gridLayout.addWidget(self.btn_stop, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 4)

        self.retranslateUi(Dialog_Remote_Control)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Remote_Control)

    def retranslateUi(self, Dialog_Remote_Control):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Remote_Control.setWindowTitle(_translate("Dialog_Remote_Control", "遥控器"))
        self.btn_ultrasonic.setText(_translate("Dialog_Remote_Control", "自动避障"))
        self.btn_surround.setText(_translate("Dialog_Remote_Control", "转圈"))
        self.btn_track.setText(_translate("Dialog_Remote_Control", "自动寻迹"))
        self.btn_speed_up.setText(_translate("Dialog_Remote_Control", "加速"))
        self.btn_speed_down.setText(_translate("Dialog_Remote_Control", "减速"))
        self.btn_left.setText(_translate("Dialog_Remote_Control", "←"))
        self.btn_right.setText(_translate("Dialog_Remote_Control", "→"))
        self.btn_backward.setText(_translate("Dialog_Remote_Control", "↓"))
        self.btn_forward.setText(_translate("Dialog_Remote_Control", "↑"))
from ui import resource_rc
