# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import paramiko
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 475)
        self.pushButton_flush = QtWidgets.QPushButton(Form)
        self.pushButton_flush.setGeometry(QtCore.QRect(680, 10, 91, 81))
        self.pushButton_flush.setObjectName("pushButton_flush")
        self.pushButton_flush.clicked.connect(self.pushButton_flush_on_click)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 661, 451))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(680, 110, 91, 41))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_flush.setText(_translate("Form", "刷新"))


    def pushButton_flush_on_click(self):
        self.pushButton_flush.setVisible(False)
        self.label.setText('正在更新')
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=, port=, username=, password=)
            stdin, stdout, stderr = ssh.exec_command('cat /home/GotIt')
            res, err = stdout.read(), stderr.read()
            result = res if res else err
            result = result.decode()
            ssh.close()
        except Exception as e:
            self.plainTextEdit.setPlainText(repr(e))
            self.label.setText('更新失败')


        self.plainTextEdit.setPlainText(result)
        self.plainTextEdit.moveCursor(QtGui.QTextCursor.End)
        # scroll_bar=self.textBrowser.verticalScrollBar()
        # scroll_bar.setValue(scroll_bar.)
        self.label.setText('更新成功')
        self.pushButton_flush.setVisible(True)

if __name__=='__main__':
    import sys
    from PyQt5.QtGui import QIcon
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('old man.jpg'))
    widget.show()
    ui.pushButton_flush_on_click()
    sys.exit(app.exec())