from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from modules import simpleQuit

class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.resize(600, 800)
        self.setMaximumSize(600, 800)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        # Logo
        lblLogo = QLabel()
        lblLogo.setPixmap("images/munchkin_logo.png")
        mainLayout.addWidget(lblLogo)

        # Add New Game widget
        self.btnNewGame = QPushButton("NEW GAME")
        self.btnNewGame.setMinimumHeight(50)
        mainLayout.addWidget(self.btnNewGame)

        # Add Load
        btnLoadGame = QPushButton("LOAD GAME")
        btnLoadGame.setMinimumHeight(50)
        mainLayout.addWidget(btnLoadGame)

        # Add players
        self.btnPlayers = QPushButton("PLAYERS")
        self.btnPlayers.setMinimumHeight(50)
        mainLayout.addWidget(self.btnPlayers)
        # btnPlayers.clicked.connect(self.ShowPlayerList)

        # Add players
        self.btnAbout = QPushButton("ABOUT")
        self.btnAbout.setMinimumHeight(50)
        mainLayout.addWidget(self.btnAbout)

        # Add quit widget
        btnQuit = QPushButton("QUIT")
        btnQuit.setMinimumHeight(50)
        mainLayout.addWidget(btnQuit)
        btnQuit.clicked.connect(self.quitGame)


    def quitGame(self):

        msgBox = simpleQuit.SimpleQuit()
        msgBox.setText("Are you sure to quit? All unsaved data will be lost!")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            # Don't save was clicked
            quit()
        elif ret == QMessageBox.Cancel:
            # cancel was clicked
            return
        else:
            pass


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    app.exec_()