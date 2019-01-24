from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

class CustomButton(QPushButton):

    def __init__(self, icon, parent=None):
        super(CustomButton, self).__init__(parent)

        self.setStyleSheet("""
            CustomButton {
                background-color: transparent;
            }
            """)

        self.setFixedWidth(50)
        self.setFixedHeight(50)
        self.setText
        img = QIcon(str(icon))
        self.setIcon(img);
        self.setIconSize(QSize(self.width(), self.height()))

