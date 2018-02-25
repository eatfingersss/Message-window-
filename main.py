# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import easygui as easygui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import _thread


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 417)
        Dialog.setAccessibleName("")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 501, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_welcome = QtWidgets.QLabel(self.frame)
        self.label_welcome.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label_welcome.setObjectName("label_welcome")

        self.label_target = QtWidgets.QLabel(self.frame)
        self.label_target.setGeometry(QtCore.QRect(60, 5, 341, 30))
        self.label_target.setText("")
        self.label_target.setObjectName("label_target")

        self.label_message = QtWidgets.QLabel(self.frame)
        self.label_message.setGeometry(QtCore.QRect(260, 40, 241, 31))

        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setBold(True)
        font.setWeight(75)

        self.label_message.setFont(font)
        self.label_message.setTabletTracking(False)
        self.label_message.setText("")
        self.label_message.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_message.setObjectName("label_message")

        self.pushButton_replace = QtWidgets.QPushButton(self.frame)
        self.pushButton_replace.setGeometry(QtCore.QRect(405, 5, 93, 30))
        self.pushButton_replace.setObjectName("pushButton_replace")

        self.button_getfile = QtWidgets.QPushButton(Dialog)
        self.button_getfile.setGeometry(QtCore.QRect(10, 380, 171, 28))
        self.button_getfile.setObjectName('button_getfile')
        self.button_getfile.setToolTip('欧拉欧拉欧拉欧拉欧拉')
        self.button_getfile.clicked.connect(self.button_getfile_on_click)

        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(370, 380, 151, 28))
        self.pushButton_exit.setObjectName('pushButton_exit')
        self.pushButton_exit.setToolTip('无駄无駄无駄无駄无駄')
        self.pushButton_exit.clicked.connect(self.pushButton_exit_on_click)

        self.pushButton_smaller = QtWidgets.QPushButton(Dialog)
        self.pushButton_smaller.setGeometry(QtCore.QRect(190, 380, 171, 28))
        self.pushButton_smaller.setObjectName('pushButton_smaller')
        self.pushButton_smaller.setToolTip('中间 (*･ω< ) ')
        self.pushButton_smaller.clicked.connect(self.pushButton_smaller_on_click)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 501, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #######################################系统托盘部分#################################
        minimizeAction = QAction('Mi&nimize', self, triggered=self.hide)
        maximizeAction = QAction('Ma&ximize', self,
                                 triggered=self.showMaximized)
        restoreAction = QAction('&Restore', self,
                                triggered=self.showNormal)
        quitAction = QAction('&Quit', self,
                             triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon('old man.jpg'))
        self.setWindowIcon(QIcon('old man.jpg'))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        # sys.exit(self.exec_())

    def file_IO(self,data):
        resfile = open('C:\\Users\\asus\\Desktop\\res.txt', 'a')
        resfile.write(str(data))
        resfile.close()
        self.label_message.setText('已导出至 C:\\Users\\asus\\Desktop\\res.txt !')
        time.sleep(2)
        self.label_message.setText('')

    def button_getfile_on_click(self):
        data=self.plainTextEdit.toPlainText()
        print('框中的内容为:'+str(data))
        try:
            _thread.start_new_thread(self.file_IO,(self,))
        except Exception as e:
           print ('Error: Can not save file :'+repr(e))
           self.label_message.setText('Error: Can not save file :'+repr(e))

    def pushButton_exit_on_click(self):
        sys.exit()

    def pushButton_smaller_on_click(self):
        self.minimumSize()
        self.minimumSizeHint()
        # self.hide()
        # self.tray = QSystemTrayIcon()  # 创建系统托盘对象
        # self.icon = QIcon('old man.jpg')  # 创建图标
        # self.tray.setIcon(self.icon)  # 设置系统托盘图标
        # self.tray.activated.connect(self.TuoPanEvent)  # 设置托盘点击事件处理函数
        # self.tray_menu = QMenu(QApplication.desktop())  # 创建菜单
        # self.RestoreAction = QAction('old man.jpg',self)  # 添加一级菜单动作选项(还原主窗口) ,triggered=self.show
        # self.QuitAction = QAction(' ', self)  # 添加一级菜单动作选项(退出程序), triggered=qApp.quit
        # self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
        # self.tray_menu.addAction(self.QuitAction)
        # self.tray.setContextMenu(self.tray_menu)  # 设置系统托盘菜单
        # pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "你们呐,Naive!"))
        self.label_welcome.setText(_translate("Dialog", "目标："))
        self.pushButton_replace.setText(_translate("Dialog", "更改"))
        self.button_getfile.setText(_translate("Dialog", "内容导出"))
        self.pushButton_exit.setText(_translate("Dialog", "退出"))
        self.pushButton_smaller.setText(_translate("Dialog", "最小化托盘"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "nothing..."))

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()

if __name__=='__main__':
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Dialog()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('old man.jpg'))
    widget.show()

    sys.exit(app.exec())