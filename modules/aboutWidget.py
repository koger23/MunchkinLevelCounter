from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class About(QWidget):

    def __init__(self, mainWindow):
        super(About, self).__init__()

        self.mainWindow = mainWindow

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)

        text = """
        This application was made for making the card game Munchkin more popular.
        It is totally free.
        I do not intend to get income with this and I do not own any rights.
        """

        lblInfo = QLabel()
        mainLayout.addWidget(lblInfo)
        lblInfo.setText(text)


        self.hide()