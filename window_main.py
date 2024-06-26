# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import icon_rc

class Ui_window_main(object):
    def setupUi(self, window_main):
        window_main.setObjectName("window_main")
        window_main.setEnabled(True)
        window_main.resize(703, 499)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_main.setWindowIcon(icon)
        window_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_info = QtWidgets.QGroupBox(window_main)
        self.groupBox_info.setGeometry(QtCore.QRect(0, 0, 181, 121))
        self.groupBox_info.setObjectName("groupBox_info")
        self.label_stuid = QtWidgets.QLabel(self.groupBox_info)
        self.label_stuid.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.label_stuid.setObjectName("label_stuid")
        self.label_pwd = QtWidgets.QLabel(self.groupBox_info)
        self.label_pwd.setGeometry(QtCore.QRect(10, 60, 31, 16))
        self.label_pwd.setObjectName("label_pwd")
        self.lineEdit_stuid = QtWidgets.QLineEdit(self.groupBox_info)
        self.lineEdit_stuid.setGeometry(QtCore.QRect(50, 30, 113, 20))
        self.lineEdit_stuid.setObjectName("lineEdit_stuid")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.groupBox_info)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(50, 60, 113, 20))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.checkBox_save = QtWidgets.QCheckBox(self.groupBox_info)
        self.checkBox_save.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.checkBox_save.setObjectName("checkBox_save")
        self.groupBox_fun = QtWidgets.QGroupBox(window_main)
        self.groupBox_fun.setGeometry(QtCore.QRect(190, 0, 161, 121))
        self.groupBox_fun.setObjectName("groupBox_fun")
        self.pushButton_getMsg = QtWidgets.QPushButton(self.groupBox_fun)
        self.pushButton_getMsg.setEnabled(False)
        self.pushButton_getMsg.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.pushButton_getMsg.setObjectName("pushButton_getMsg")
        self.pushButton_autoEnroll = QtWidgets.QPushButton(self.groupBox_fun)
        self.pushButton_autoEnroll.setEnabled(False)
        self.pushButton_autoEnroll.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.pushButton_autoEnroll.setObjectName("pushButton_autoEnroll")
        self.pushButton_login = QtWidgets.QPushButton(self.groupBox_fun)
        self.pushButton_login.setEnabled(True)
        self.pushButton_login.setGeometry(QtCore.QRect(40, 20, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.textBrowser_log = QtWidgets.QTextBrowser(window_main)
        self.textBrowser_log.setEnabled(True)
        self.textBrowser_log.setGeometry(QtCore.QRect(360, 10, 331, 101))
        self.textBrowser_log.setObjectName("textBrowser_log")
        self.listWidget = QtWidgets.QListWidget(window_main)
        self.listWidget.setGeometry(QtCore.QRect(0, 120, 691, 371))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(window_main)
        QtCore.QMetaObject.connectSlotsByName(window_main)

    def retranslateUi(self, window_main):
        _translate = QtCore.QCoreApplication.translate
        window_main.setWindowTitle(_translate("window_main", "Snatch Lecture"))
        self.groupBox_info.setTitle(_translate("window_main", "基本信息"))
        self.label_stuid.setText(_translate("window_main", "学号："))
        self.label_pwd.setText(_translate("window_main", "密码："))
        self.checkBox_save.setText(_translate("window_main", "保存并自动登录"))
        self.groupBox_fun.setTitle(_translate("window_main", "功能界面"))
        self.pushButton_getMsg.setText(_translate("window_main", "已报讲座"))
        self.pushButton_autoEnroll.setText(_translate("window_main", "自动报名"))
        self.pushButton_login.setText(_translate("window_main", "登录"))
