from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

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
            self.mainWindow.playerList.btnRemovePlayer.show()
            self.mainWindow.playerList.btnEditPlayer.show()
            self.mainWindow.playerList.btnAddPlayer.show()
        elif ret == QMessageBox.Cancel:
            # cancel was clicked
            return
        else:
            pass