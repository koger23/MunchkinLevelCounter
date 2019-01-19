#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide2.QtGui import QFontDatabase
from modules import simpleQuit, playerList, mainMenu

class LevelCounter(QMainWindow):

    def __init__(self):
        super(LevelCounter, self).__init__()
        self.setWindowTitle("Level counter v0.1")
        self.resize(600, 700)
        self.setMaximumSize(600, 700)

        self.centralWidget = QWidget()
        mainLayout = QVBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        # Main Menu
        self.mainMenu = mainMenu.MainMenu()
        mainLayout.addWidget(self.mainMenu)
        self.mainMenu.btnPlayers.clicked.connect(self.showPlayerList)
        self.mainMenu.setVisible(True)

        # Player List
        self.playerList = playerList.PlayerList()
        mainLayout.addWidget(self.playerList)
        self.playerList.hide()

        # Navigation button
        self.btnBack = QPushButton("Back")
        mainLayout.addWidget(self.btnBack)
        self.btnBack.clicked.connect(self.backToMainMenu)
        self.btnBack.hide()


        self.applyStyle()

    def showPlayerList(self):

        print("TIME")
        self.mainMenu.hide()
        self.btnBack.show()
        self.playerList.show()

    def backToMainMenu(self):
        self.mainMenu.show()
        self.btnBack.hide()
        self.playerList.hide()


    def applyStyle(self):

        QFontDatabase.addApplicationFont("images/adobekaiti.ttf")
        with open("images/style.qss", "r") as styleFile:
            style = styleFile.read()

        self.setStyleSheet(style)


app = QApplication(sys.argv)
window = LevelCounter()
window.show()
app.exec_()