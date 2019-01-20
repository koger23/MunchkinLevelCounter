from PySide2.QtWidgets import QPushButton, QWidget
from PySide2.QtGui import QBrush, QPen, QColor, QPainter, QFont
from PySide2.QtCore import Qt
import numpy as np


class MunchkinButton(QPushButton):

    def __init__(self, w, h, parent=None):

        super(MunchkinButton, self).__init__(parent)

        self.w = w
        self.h = h
        self.text = "test"

        self.font = QFont()
        self.font.setPointSize(30)
        self.font.setBold(True)

    def paintEvent(self, e):
        qp = QPainter(self)
        # Draw circle
        qp.setPen(QColor("#999999"))
        qp.setBrush(QColor("#3e2723"))
        qp.drawEllipse(0, 0, self.w - 2, self.h - 2)

        # Draw text
        qp.setFont(self.font)
        qp.setBrush(QColor("#999999"))
        qp.drawText(8, 37, "-")

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Points')
        # self.drawP()


    # def drawP(self):
    #     t = MunchkinButton(50, 50, parent=self)
    #     t.setGeometry(50, 50, 50, 50)
    #     t.clicked.connect(self.test)
    #
    # def test(self):
    #
    #     print("test")

if __name__ == '__main__':

    import sys
    from PySide2.QtWidgets import QApplication, QWidget



    app = QApplication(sys.argv)
    window = Example()
    window.show()
    app.exec_()