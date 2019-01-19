from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide2.QtGui import QFontDatabase

class LoadGameWidget(QWidget):


    def __init__(self):
        super(LoadGameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)

        QFontDatabase.addApplicationFont("images/adobekaiti.ttf")