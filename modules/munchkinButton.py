from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QFontDatabase


class MunchkinButton(QPushButton):

    def __init__(self, text):

        super(MunchkinButton, self).__init__(text)

        self.applyStyle()

    def applyStyle(self):
        QFontDatabase.addApplicationFont("images/adobekaiti.ttf")
        with open("images/style.qss", "r") as styleFile:
            style = styleFile.read()

        self.setStyleSheet(style)



