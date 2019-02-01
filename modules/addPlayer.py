from PySide2.QtWidgets import QWidget, QRadioButton, QLabel, QTextEdit, QMessageBox, QHBoxLayout, QPushButton, QGridLayout
from PySide2.QtCore import Qt
from utils import DB_utils as dbu

class AddPlayer(QWidget):

    def __init__(self, playerList, parent=None):

        super(AddPlayer, self).__init__(parent)

        self.playerList = playerList

        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        # self.setMaximumSize(600, 270)
        # self.setMinimumSize(600, 100)
        # self.resize(600, 270)
        self.setLayout(mainLayout)

        baseLayout = QGridLayout()
        mainLayout.addLayout(baseLayout)

        # Labels
        lblPlayerName = QLabel("Player name:")
        lblPlayerName.setObjectName("addPlayerLabels")
        baseLayout.addWidget(lblPlayerName, 0, 0)

        lblGender = QLabel("Gender:")
        lblGender.setObjectName("addPlayerLabels")
        baseLayout.addWidget(lblGender, 1, 0)

        lblPlayerGames = QLabel("Games played:")
        lblPlayerGames.setObjectName("addPlayerLabels")
        baseLayout.addWidget(lblPlayerGames, 2, 0)

        lblGamesWon = QLabel("Games won:")
        lblGamesWon.setObjectName("addPlayerLabels")
        baseLayout.addWidget(lblGamesWon, 3, 0)

        lblPlayedRounds = QLabel("Rounds played:")
        lblPlayedRounds.setObjectName("addPlayerLabels")
        baseLayout.addWidget(lblPlayedRounds, 4, 0)

        # Text fields
        self.txtPlayerName = QTextEdit()
        self.txtPlayerName.setObjectName("addPlayer_txtField")
        baseLayout.addWidget(self.txtPlayerName, 0, 1, 1, 2)
        self.txtPlayerName.setFixedHeight(35)

        self.rbtnMale = QRadioButton("Male")
        self.rbtnMale.setObjectName("addPlayerRadioBtn")
        baseLayout.addWidget(self.rbtnMale, 1, 1, alignment=Qt.AlignCenter)
        self.rbtnMale.setChecked(True)

        self.rbtnFemale = QRadioButton("Female")
        self.rbtnFemale.setObjectName("addPlayerRadioBtn")
        baseLayout.addWidget(self.rbtnFemale, 1, 2)

        self.txtPlayerGames = QTextEdit("0")
        self.txtPlayerGames.setObjectName("addPlayer_txtField")
        baseLayout.addWidget(self.txtPlayerGames, 2, 1, 1, 2)
        self.txtPlayerGames.setFixedHeight(35)

        self.txtPlayerWins = QTextEdit("0")
        self.txtPlayerWins.setObjectName("addPlayer_txtField")
        baseLayout.addWidget(self.txtPlayerWins, 3, 1, 1, 2)
        self.txtPlayerWins.setFixedHeight(35)

        self.txtPlayedRounds = QTextEdit("0")
        self.txtPlayedRounds.setObjectName("addPlayer_txtField")
        baseLayout.addWidget(self.txtPlayedRounds, 4, 1, 1, 2)
        self.txtPlayedRounds.setFixedHeight(35)
        self.txtPlayedRounds.setEnabled(False)

        # Buttons
        btnSavePlayer = QPushButton("Save")
        btnSavePlayer.setFixedHeight(50)
        baseLayout.addWidget(btnSavePlayer, 5, 0)
        btnSavePlayer.clicked.connect(self.savePlayer)

        btnCancel = QPushButton("Cancel")
        btnCancel.setFixedHeight(50)
        baseLayout.addWidget(btnCancel, 5, 1)
        btnCancel.clicked.connect(self.cancel)

    def clearAll(self):

        self.txtPlayerName.clear()
        self.txtPlayerWins.clear()
        self.txtPlayerGames.clear()

    def cancel(self):
        self.hide()
        self.playerList.btnAddPlayer.show()
        self.playerList.btnEditPlayer.show()
        self.playerList.browser.show()
        self.playerList.btnRemovePlayer.show()
        self.playerList.mainWindow.btnBack.show()
        self.playerList.mainWindow.btnStartGame.show()

        self.playerList.setMaximumSize(600, 800)
        self.playerList.browser.refreshView()


    def savePlayer(self):

        name = self.txtPlayerName.toPlainText()

        # check name
        if name:
            if len(name) < 1:
                raise TypeError
        else:
            msg1 = QMessageBox()
            msg1.setText("Player name is not given.")
            msg1.exec_()
            return

        # Check radiobuttons value
        if self.rbtnMale.isChecked():
            gender = "male"
        elif self.rbtnFemale.isChecked():
            gender = "female"
        else:
            msg1 = QMessageBox()
            msg1.setText("Select gender.")
            msg1.exec_()

        gamesPlayed = self.txtPlayerGames.toPlainText()

        # Check games played
        if gamesPlayed:

            try:
                gamesPlayed = int(gamesPlayed)

                if gamesPlayed < 0:
                    raise TypeError
                else:
                    gamesPlayed = str(gamesPlayed)
            except:
                msg2 = QMessageBox()
                msg2.setText("Invalid number in Games played.\n\nValid: 0-9999")
                msg2.exec_()
                return
        else:
            msg2 = QMessageBox()
            msg2.setText("Number of played games is not given.")
            msg2.exec_()
            return


        wins = self.txtPlayerWins.toPlainText()

        # Check number of wins
        if wins:
            try:
                wins = int(wins)
                if wins < 0:
                    raise TypeError
                else:
                    wins = str(wins)
            except:
                msg3 = QMessageBox()
                msg3.setText("Invalid number in Wins field.\n\nValid: 0-9999")
                msg3.exec_()
                return
        else:
            msg3 = QMessageBox()
            msg3.setText("Number of won games is not given.")
            msg3.exec_()
            return

        dbu.Database().addPlayer(name, gender, gamesPlayed, wins, 0)


        self.hide()
        self.playerList.btnAddPlayer.show()
        self.playerList.btnEditPlayer.show()
        self.playerList.browser.show()
        self.playerList.btnRemovePlayer.show()
        self.playerList.mainWindow.btnBack.show()
        self.playerList.mainWindow.btnStartGame.show()

        self.playerList.setMaximumSize(600, 800)
        self.playerList.browser.refreshView()


class EditPlayer(AddPlayer):

    def __init__(self, playerList, parent=None):

        super(EditPlayer, self).__init__(playerList, parent)
        self.txtPlayedRounds.setEnabled(True)

    def getInputs(self):

        # Get selected object name, wins, games and gender
        self.name = self.playerList.browser.currentItem().playerObject.name
        self.wins = str(self.playerList.browser.currentItem().playerObject.wins)
        self.games = str(self.playerList.browser.currentItem().playerObject.games)
        self.gender = self.playerList.browser.currentItem().playerObject.gender
        self.rounds = str(self.playerList.browser.currentItem().playerObject.rounds)

        self.txtPlayerName.setText(self.name)
        self.txtPlayerWins.setText(self.wins)
        self.txtPlayerGames.setText(self.games)
        self.txtPlayedRounds.setText(self.rounds)

        if self.gender == "male":
            self.rbtnMale.setChecked(True)
            self.rbtnFemale.setChecked(False)

        else:
            self.rbtnMale.setChecked(False)
            self.rbtnFemale.setChecked(True)

    def savePlayer(self):

        name = self.txtPlayerName.toPlainText()

        # check name
        if name:
            if len(name) < 1:
                raise TypeError
        else:
            msg1 = QMessageBox()
            msg1.setText("Player name is not given.")
            msg1.exec_()
            return

        # Check radiobuttons value
        if self.rbtnMale.isChecked():
            gender = "male"
        elif self.rbtnFemale.isChecked():
            gender = "female"
        else:
            msg1 = QMessageBox()
            msg1.setText("Select gender.")
            msg1.exec_()

        gamesPlayed = self.txtPlayerGames.toPlainText()

        # Check games played
        if gamesPlayed:

            try:
                gamesPlayed = int(gamesPlayed)

                if gamesPlayed < 0:
                    raise TypeError
                else:
                    gamesPlayed = str(gamesPlayed)
            except:
                msg2 = QMessageBox()
                msg2.setText("Invalid number in Games played.\n\nValid: 0-9999")
                msg2.exec_()
                return
        else:
            msg2 = QMessageBox()
            msg2.setText("Number of played games is not given.")
            msg2.exec_()
            return

        wins = self.txtPlayerWins.toPlainText()

        # Check number of wins
        if wins:
            try:
                wins = int(wins)
                if wins < 0:
                    raise TypeError
                else:
                    wins = str(wins)
            except:
                msg3 = QMessageBox()
                msg3.setText("Invalid number in Wins field.\n\nValid: 0-9999")
                msg3.exec_()
                return
        else:
            msg3 = QMessageBox()
            msg3.setText("Number of won games is not given.")
            msg3.exec_()
            return

        id = dbu.Database().getPlayerId(self.name,
                                        self.games,
                                        self.wins)[0][0]

        dbu.Database().updateAll(id, self.txtPlayerName.toPlainText(),
                              str(gender),
                              int(self.txtPlayerGames.toPlainText()),
                              int(self.txtPlayerWins.toPlainText()),
                              int(self.txtPlayedRounds.toPlainText()))


        self.hide()
        self.playerList.btnAddPlayer.show()
        self.playerList.btnEditPlayer.show()
        self.playerList.browser.show()
        self.playerList.btnRemovePlayer.show()
        self.playerList.mainWindow.btnBack.show()
        self.playerList.mainWindow.btnStartGame.show()

        self.playerList.setMaximumSize(600, 800)

        self.playerList.browser.refreshView()


if __name__ == '__main__':

    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = AddPlayer()
    window.show()
    app.exec_()