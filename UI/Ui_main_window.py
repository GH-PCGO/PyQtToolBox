# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 539)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 692, 502))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(180, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(400, 300))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_4.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(400, 150))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_4.addWidget(self.plainTextEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(700, 0, 77, 69))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_6.addWidget(self.checkBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(700, 370, 109, 125))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_7.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_7.addWidget(self.checkBox_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_7.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "蓝牙设置"))
        self.label.setText(_translate("MainWindow", "设备："))
        self.label_2.setText(_translate("MainWindow", "状态："))
        self.pushButton.setText(_translate("MainWindow", "点击连接"))
        self.groupBox_2.setTitle(_translate("MainWindow", "已连接的设备："))
        self.label_3.setText(_translate("MainWindow", "名称："))
        self.label_5.setText(_translate("MainWindow", "地址："))
        self.label_6.setText(_translate("MainWindow", "空"))
        self.label_4.setText(_translate("MainWindow", "空"))
        self.checkBox.setText(_translate("MainWindow", "HEX显示"))
        self.checkBox_2.setText(_translate("MainWindow", "加时间戳"))
        self.pushButton_3.setText(_translate("MainWindow", "清空接收区"))
        self.pushButton_4.setText(_translate("MainWindow", "清空发送"))
        self.checkBox_3.setText(_translate("MainWindow", "HEX发送"))
        self.checkBox_4.setText(_translate("MainWindow", "自动加回车换行"))
        self.pushButton_5.setText(_translate("MainWindow", "发送"))