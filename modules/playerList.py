#!/usr/bin/env python3
from PySide2.QtWidgets import QApplication, QWidget, QListWidget, QStyledItemDelegate, QVBoxLayout, QStyle, QListWidgetItem, QPushButton, QHBoxLayout
from PySide2.QtGui import QIcon, QBrush, QColor, QPen, QPixmap, QFont
from PySide2.QtCore import QSize, QRect, Qt

import sys
from utils import DB_utils as dbu
from modules import addPlayer
from objects import players as ply

class PlayerList(QWidget):

    def __init__(self, mainWindow, parent=None):

        super(PlayerList, self).__init__(parent)
        self.mainWindow = mainWindow
        # self.resize(600, 700)
        # self.setMaximumSize(600, 700)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        addPlayerLayout = QHBoxLayout()
        mainLayout.addLayout(addPlayerLayout)

        self.btnAddPlayer = QPushButton("Add Player")
        addPlayerLayout.addWidget(self.btnAddPlayer)
        self.btnAddPlayer.clicked.connect(self.addPlayer)
        self.btnAddPlayer.setMinimumHeight(50)

        self.btnEditPlayer = QPushButton("Edit Player")
        addPlayerLayout.addWidget(self.btnEditPlayer)
        self.btnEditPlayer.setMinimumHeight(50)
        self.btnEditPlayer.clicked.connect(self.editPlayer)

        self.btnRemovePlayer = QPushButton("Remove Player")
        addPlayerLayout.addWidget(self.btnRemovePlayer)
        self.btnRemovePlayer.clicked.connect(self.removePlayer)
        self.btnRemovePlayer.setMinimumHeight(50)

        self.browser = PlayerBrowser()
        mainLayout.addWidget(self.browser)

        self.addPlayerWidget = addPlayer.AddPlayer(self)
        mainLayout.addWidget(self.addPlayerWidget)
        self.addPlayerWidget.hide()

        self.editPlayerWidget = addPlayer.EditPlayer(self)
        mainLayout.addWidget(self.editPlayerWidget)
        self.editPlayerWidget.hide()

        self.browser.refreshView()

    def addPlayer(self):

        self.addPlayerWidget.clearAll()
        self.addPlayerWidget.show()
        self.btnAddPlayer.hide()
        self.btnEditPlayer.hide()
        self.browser.hide()
        self.btnRemovePlayer.hide()
        self.mainWindow.btnStartGame.hide()
        self.mainWindow.btnBack.hide()

        self.setMaximumSize(600, 250)

        self.browser.refreshView()

    def editPlayer(self):

        self.editPlayerWidget.getInputs()
        self.editPlayerWidget.show()
        self.btnAddPlayer.hide()
        self.btnEditPlayer.hide()
        self.browser.hide()
        self.btnRemovePlayer.hide()
        self.mainWindow.btnStartGame.hide()
        self.mainWindow.btnBack.hide()

        self.setMaximumSize(600, 250)

        self.browser.refreshView()

    def removePlayer(self):

        dbu.Database().removePlayer(self.browser.getCurrentPlayer().name,
                                    self.browser.getCurrentPlayer().games,
                                    self.browser.getCurrentPlayer().wins)
        self.browser.refreshView()

class PlayerBrowser(QListWidget):

    def __init__(self):
        super(PlayerBrowser, self).__init__()

        self.setMovement(QListWidget.Static)
        self.setResizeMode(QListWidget.Adjust)
        self.setSelectionMode(QListWidget.ExtendedSelection)
        self.setSpacing(5)

        self.setItemDelegate(MyDelegate())

        self.currentPlayer = None

        self.itemClicked.connect(self.setCurrentPlayer)

    def getCurrentPlayer(self):

        return self.currentPlayer

    def setCurrentPlayer(self):

        self.currentPlayer = self.currentItem().playerObject


    def refreshView(self):

        self.clear()

        self.playerObjects = []

        # Get player names
        players = dbu.Database().getPlayerNames()

        for name in players:
            # Fill the list with player names

            player = dbu.Database().getPlayerByName(name[0]) # get all players

            playerObj = ply.Player(player[0][1]) # create player objects
            # set players stats
            playerObj.setGender(player[0][2])
            playerObj.setRounds(player[0][3])
            playerObj.setWins(player[0][4])
            playerObj.setAvatar()

            # create list item
            PlayerItem(playerObj, self)

            self.playerObjects.append(playerObj)

class PlayerItem(QListWidgetItem):

    def __init__(self, playerObject, parent):

        super(PlayerItem, self).__init__(parent)

        self.playerObject = playerObject

        self.setToolTip(playerObject.name + ": Wins: " + str(playerObject.games) + "/" + str(playerObject.wins))

        # set size
        self.setSizeHint(QSize(100, 140))
        # passing player object to delegate
        self.setData(Qt.UserRole, playerObject)

class MyDelegate(QStyledItemDelegate):

    def __init__(self):
        super(MyDelegate, self).__init__()

        self.bgColor = QBrush(QColor("#fad7a0"))
        self.name = QPen(QColor("#5555"))

        self.fontPlayerName = QFont()
        self.fontPlayerName.setPointSize(20)
        self.fontPlayerName.setBold(True)

        self.fontPlayerTotal = QFont()
        self.fontPlayerTotal.setPointSize(20)
        self.fontPlayerTotal.setBold(True)

        self.fontPlayerTotalValue = QFont()
        self.fontPlayerTotalValue.setPointSize(36)
        self.fontPlayerTotalValue.setBold(True)

        self.fontPlayerLevel = QFont()
        self.fontPlayerLevel.setPointSize(14)
        self.fontPlayerLevel.setBold(False)

        self.selectedColor = QBrush(QColor("#bcaaa4"))

    def paint(self, painter, option, index):
        rect = option.rect

        playerObject = index.data(Qt.UserRole)

        if option.state & QStyle.State_Selected:
            painter.setBrush(self.selectedColor)
        else:
            painter.setBrush(self.bgColor)

        # Background
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

        # avatar
        pixmap = QPixmap(playerObject.avatar).scaledToHeight(128, Qt.SmoothTransformation)
        pixmapRect = QRect(rect.x()+10, rect.y()+8, pixmap.width(), pixmap.height())
        painter.drawPixmap(pixmapRect, pixmap)

        # Player name
        painter.setFont(self.fontPlayerName)
        painter.setPen(self.name)
        nameRect = QRect(rect.x()+110, pixmapRect.top(), 100, 40)
        painter.drawText(nameRect, Qt.AlignLeft | Qt.AlignVCenter, playerObject.name)

        # Draw ingame stats if players in game
        if playerObject.inGame == 1:
            # Player Level:
            painter.setFont(self.fontPlayerTotal)
            painter.setPen(self.name)
            levelRect = QRect(nameRect.right()+70, pixmapRect.top(), 100, 40)
            painter.drawText(levelRect, Qt.AlignHCenter | Qt.AlignVCenter, "Level")
            painter.setFont(self.fontPlayerTotalValue)
            levelValRect = QRect(levelRect.left(), levelRect.bottom()+20, 100, 40)
            painter.drawText(levelValRect, Qt.AlignHCenter | Qt.AlignVCenter, str(playerObject.currentLevel))

            # Player Bonus:
            painter.setFont(self.fontPlayerTotal)
            painter.setPen(self.name)
            bonusRect = QRect(levelRect.right()+50, pixmapRect.top(), 100, 40)
            painter.drawText(bonusRect, Qt.AlignHCenter | Qt.AlignVCenter, "Bonus")
            painter.setFont(self.fontPlayerTotalValue)
            bonusValRect = QRect(levelRect.right()+50, levelRect.bottom()+20, 100, 40)
            painter.drawText(bonusValRect, Qt.AlignHCenter | Qt.AlignVCenter, str(playerObject.currentBonus))

            # Player Total:
            painter.setFont(self.fontPlayerTotal)
            painter.setPen(self.name)
            totalRect = QRect(bonusRect.right()+50, pixmapRect.top(), 100, 40)
            painter.drawText(totalRect, Qt.AlignHCenter | Qt.AlignVCenter, "Total")
            painter.setFont(self.fontPlayerTotalValue)
            totalValRect = QRect(bonusRect.right()+50, bonusRect.bottom()+20, 100, 40)
            painter.drawText(totalValRect, Qt.AlignHCenter | Qt.AlignVCenter, str(playerObject.currentLevel + playerObject.currentBonus))

        # Player bonus
        painter.setFont(self.fontPlayerLevel)
        bonusRect = QRect(nameRect.x(), pixmapRect.top()+40, 70, 20)
        painter.drawText(bonusRect, Qt.AlignLeft | Qt.AlignVCenter, "Gender:")
        bonusValRect = QRect(bonusRect.right()+5, pixmapRect.top()+40, 100, 20)
        painter.drawText(bonusValRect, Qt.AlignLeft | Qt.AlignVCenter, str(playerObject.gender))

        # Player played games
        painter.setFont(self.fontPlayerLevel)
        roundsRect = QRect(nameRect.x(), bonusRect.bottom(), 70, 20)
        painter.drawText(roundsRect, Qt.AlignLeft | Qt.AlignVCenter, "Games:")
        roundsValRect = QRect(nameRect.left(), bonusRect.bottom(), 100, 20)
        painter.drawText(roundsValRect, Qt.AlignRight | Qt.AlignVCenter, str(playerObject.games))

        # Player wins
        painter.setFont(self.fontPlayerLevel)
        winsRect = QRect(nameRect.x(), roundsRect.bottom(), 70, 20)
        painter.drawText(winsRect, Qt.AlignLeft | Qt.AlignVCenter, "Wins:")
        winsValRect = QRect(nameRect.left(), roundsRect.bottom(), 100, 20)
        painter.drawText(winsValRect, Qt.AlignRight | Qt.AlignVCenter, str(playerObject.wins))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = PlayerList()
    window.show()
    app.exec_()