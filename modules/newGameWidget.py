from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide2.QtGui import QFontDatabase


class NewGameWidget(QWidget):


    def __init__(self):
        super(NewGameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)


        QFontDatabase.addApplicationFont("images/adobekaiti.ttf")