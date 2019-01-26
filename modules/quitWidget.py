from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from utils import DB_utils as dbu

class QuitWidget(QWidget):


    def __init__(self, mainWindow):
        super(QuitWidget, self).__init__()
        self.mainWindow = mainWindow

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)

        btnQuit = QPushButton("QUIT")
        btnQuit.setMinimumHeight(50)
        mainLayout.addWidget(btnQuit)
        btnQuit.clicked.connect(self.quitMsg)


    def quitMsg(self):

        msgBox = QMessageBox()
        msgBox.setText("Are you sure to quit? All unsaved data will be lost!")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()

        if ret == QMessageBox.Save:
            # Save was clicked - save game dialog
            pass

        elif ret == QMessageBox.Discard:
            # Don't save was clicked - exitting into main menu
            self.mainWindow.backToMainMenu()
            self.mainWindow.btnQuit.hide()
            self.mainWindow.playerList.btnRemovePlayer.hide()
            self.mainWindow.playerList.btnEditPlayer.hide()
            self.mainWindow.playerList.btnAddPlayer.hide()

            if self.mainWindow.gameWidget.isVisible():

                for i in self.mainWindow.playerList.browser.playerObjects:

                    print(i.name)
                    print(i.currentLevel)
                    print(i.currentBonus)
                    print(int(i.rounds) + int(self.mainWindow.gameWidget.game.rounds))
                    print("--")

                    rounds = int(i.rounds) + int(self.mainWindow.gameWidget.game.rounds)

                    print("rounds: " + str(rounds))

                    dbu.Database().update(id=i.id,
                                          name=i.name,
                                          gamesplayed=int(i.games),
                                          wins=int(i.wins),
                                          roundsplayed=int(rounds))

                self.mainWindow.gameWidget.hide()

            self.mainWindow.setMaximumSize(600, 800)
            self.mainWindow.setMinimumSize(600, 800)
            self.mainWindow.resize(600, 800)



        elif ret == QMessageBox.Cancel:
            # cancel was clicked
            self.mainWindow.gameWidget.setVisible(True)
            return
        else:
            pass