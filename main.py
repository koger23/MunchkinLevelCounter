#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide2.QtGui import QFontDatabase
from modules import playerList, mainMenu, quitWidget, gameWidget
from objects import game

class LevelCounter(QMainWindow):

    def __init__(self):
        super(LevelCounter, self).__init__()
        self.setWindowTitle("Level counter v0.1")
        self.resize(600, 800)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)

        self.centralWidget = QWidget()
        baseLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        mainLayout = QVBoxLayout()
        baseLayout.addLayout(mainLayout)

        # Main Menu
        self.mainMenu = mainMenu.MainMenu()
        mainLayout.addWidget(self.mainMenu)
        self.mainMenu.btnPlayers.clicked.connect(self.showPlayerList)
        self.mainMenu.btnNewGame.clicked.connect(self.newGame)
        self.mainMenu.setVisible(True)

        # Player List
        self.playerList = playerList.PlayerList(self)
        mainLayout.addWidget(self.playerList)
        self.playerList.hide()

        # Game object to count rounds
        self.game = game.Game()

        # Game Widget
        self.gameWidget = gameWidget.GameWidget(self.game)
        baseLayout.addWidget(self.gameWidget)
        self.gameWidget.setVisible(False)


        # Get on signals for buttons in Game
        self.gameWidget.bonusCounterWidget.btnBonusInc.clicked.connect(self.playerList.increasePlayerBonus)
        self.gameWidget.bonusCounterWidget.btnBonusDec.clicked.connect(self.playerList.decreasePlayerBonus)
        self.gameWidget.levelCounterWidget.btnLevelInc.clicked.connect(self.playerList.increasePlayerLevel)
        self.gameWidget.levelCounterWidget.btnLevelDec.clicked.connect(self.playerList.decreasePlayerLevel)
        self.gameWidget.btnNextPlayer.clicked.connect(self.gameWidget.game.increaseRounds)
        self.gameWidget.btnNextPlayer.clicked.connect(self.playerList.browser.nextItem)

        # Navigation buttons
        self.btnBack = QPushButton("Back")
        mainLayout.addWidget(self.btnBack)
        self.btnBack.clicked.connect(self.backToMainMenu)
        self.btnBack.setMinimumHeight(50)
        self.btnBack.hide()

        self.btnStartGame = QPushButton("Start Game")
        mainLayout.addWidget(self.btnStartGame)
        self.btnStartGame.clicked.connect(self.startGame)
        self.btnStartGame.setMinimumHeight(50)
        self.btnStartGame.hide()

        self.btnQuit = QPushButton("Leave Game")
        mainLayout.addWidget(self.btnQuit)
        self.btnQuit.setMinimumHeight(50)
        self.btnQuit.clicked.connect(self.leaveGame)
        self.btnQuit.hide()

        self.applyStyle()

    def showPlayerList(self):

        self.mainMenu.hide()
        self.btnBack.show()
        self.playerList.show()
        self.playerList.browser.refreshView()

    def backToMainMenu(self):

        self.mainMenu.show()
        self.btnBack.hide()
        self.playerList.hide()
        self.btnStartGame.hide()

        if self.playerList.addPlayerWidget.isVisible():
            self.playerList.addPlayerWidget.hide()

        self.resize(600, 700)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)

    def newGame(self):

        self.mainMenu.hide()
        self.btnBack.show()
        self.btnStartGame.show()
        self.playerList.show()
        self.playerList.browser.refreshView()

    def startGame(self):

        # Get selected players for new game
        selectedItems = self.playerList.browser.selectedItems()

        if len(selectedItems) > 1:

            for i in selectedItems:
                    i.playerObject.inGame = 1 # select for new game

            # Get all item in list
            items = []
            for index in range(self.playerList.browser.count()):
                items.append(self.playerList.browser.item(index))

            # hide items which are not selected for new game
            for item in items:
                if item.playerObject.inGame == 0:
                    self.playerList.browser.takeItem(self.playerList.browser.row(item))

            self.setMaximumSize(1500, 750)
            self.setMinimumSize(1500, 750)
            self.resize(1500, 750)

            self.playerList.btnRemovePlayer.hide()
            self.playerList.btnEditPlayer.hide()
            self.playerList.btnAddPlayer.hide()

            self.gameWidget.setVisible(True)

            self.btnStartGame.hide()
            self.btnBack.hide()
            self.btnQuit.show()

    def leaveGame(self):

        quitWidget.QuitWidget(self).quitMsg()
        self.gameWidget.setVisible(False)

    def applyStyle(self):

        QFontDatabase.addApplicationFont("images/adobekaiti.ttf")
        with open("images/style.qss", "r") as styleFile:
            style = styleFile.read()

        self.setStyleSheet(style)


app = QApplication(sys.argv)
window = LevelCounter()
window.show()
app.exec_()