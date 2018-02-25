from signal import signal

import sys
from PyQt5.QtCore import QPropertyAnimation, QPoint, QTimer, pyqtSlot
from PyQt5.QtWidgets import QDesktopWidget, QDialog
from PyQt5.uic.properties import QtGui, QtWidgets
from PyQt5 import QtGui,QtCore


class Message(QDialog):
    def __init__(self):
        self.desktop = QDesktopWidget()
        self.move((self.desktop.availableGeometry().width() - self.width()),
        self.desktop.availableGeometry().height())  # 初始化位置到右下角
        self.showAnimation()



    # 弹出动画
    def showAnimation(self):
        # 显示弹出框动画
        self.animation = QPropertyAnimation(self, "pos")
        self.animation.setDuration(1000)
        self.animation.setStartValue(QPoint(self.x(), self.y()))
        self.animation.setEndValue(QPoint((self.desktop.availableGeometry().width() - self.width()),
        (self.desktop.availableGeometry().height() - self.height() + self.SHADOW_WIDTH)))
        self.animation.start()

    # 设置弹出框1秒弹出，然后渐隐
        self.remainTimer = QTimer()
        self.connect(self.remainTimer, signal("timeout()"), self, signal.__slots__("closeAnimation()"))
        self.remainTimer.start(10000)  # 定时器10秒


# 关闭动画
    @pyqtSlot()
    def closeAnimation(self):
        # 清除Timer和信号槽
        self.remainTimer.stop()
        self.disconnect(self.remainTimer, signal("timeout()"), self, signal.__slots__("closeAnimation()"))
        self.remainTimer.deleteLater()
        self.remainTimer = None
        # 弹出框渐隐
        self.animation = QPropertyAnimation(self, "windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()
        # 动画完成后清理
        self.connect(self.animation, signal("finished()"), self, signal.__slots__("clearAll()"))


    # 清理及退出
    def clearAll(self):
        self.disconnect(self.animation,signal("finished()"), self,signal.__slots__("clearAll()"))
        sys.exit()  # 退出

if __name__=='__main__':
    x=Message()