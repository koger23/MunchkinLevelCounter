from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PySide2.QtGui import QIcon, QFontDatabase
from modules.customButtons import CustomButton


class GameWidget(QWidget):


    def __init__(self, gameObj):
        super(GameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        mainLayout.setContentsMargins(10, 10, 0, 0)
        # self.resize(600, 800)
        # self.setMinimumSize(600, 800)
        # self.setMaximumSize(600, 800)

        # Game object to count rounds
        self.game = gameObj

        # Round
        self.roundNumber = 1
        lblRounds = QLabel("Round: " + str(self.game.rounds))
        lblRounds.setObjectName("RoundCounter")
        mainLayout.addWidget(lblRounds)


        # Counters
        counterLayout = QHBoxLayout()
        mainLayout.addLayout(counterLayout)

        self.bonusCounterWidget = BonusCountWidget()
        counterLayout.addWidget(self.bonusCounterWidget)

        self.levelCounterWidget = LevelCountWidget()
        counterLayout.addWidget(self.levelCounterWidget)

        # Next Player Button
        self.btnNextPlayer = QPushButton("Next Player")
        self.btnNextPlayer.setMinimumHeight(50)
        mainLayout.addWidget(self.btnNextPlayer)

    def increaseGameRounds(self):

        self.game.increaseRounds()
        self.repaint()


class BonusCountWidget(QWidget):

    def __init__(self):
        super(BonusCountWidget, self).__init__()
        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        self.setMaximumHeight(150)
        mainLayout.setContentsMargins(10, 10, 10, 10)

        buttonsLayout = QHBoxLayout()
        mainLayout.addLayout(buttonsLayout)

        bonusLayout = QVBoxLayout()
        buttonsLayout.addLayout(bonusLayout)
        levelLayout = QVBoxLayout()
        buttonsLayout.addLayout(levelLayout)

        self.btnBonusInc = CustomButton("images/icon_plus.png")
        bonusLayout.addWidget(self.btnBonusInc)

        lblBonus = QLabel("Bonus")
        lblBonus.setObjectName("bonusLabel")
        bonusLayout.addWidget(lblBonus)

        self.btnBonusDec = CustomButton("images/icon_minus.png")
        bonusLayout.addWidget(self.btnBonusDec)


class LevelCountWidget(QWidget):

    def __init__(self):
        super(LevelCountWidget, self).__init__()
        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        self.setMaximumHeight(150)
        mainLayout.setContentsMargins(10, 10, 10, 10)

        buttonsLayout = QHBoxLayout()
        mainLayout.addLayout(buttonsLayout)

        bonusLayout = QVBoxLayout()
        buttonsLayout.addLayout(bonusLayout)
        levelLayout = QVBoxLayout()
        buttonsLayout.addLayout(levelLayout)

        self.btnLevelInc = CustomButton("images/icon_plus.png")
        levelLayout.addWidget(self.btnLevelInc)

        lblLevel = QLabel("Level")
        lblLevel.setObjectName("bonusLabel")
        levelLayout.addWidget(lblLevel)

        self.btnLevelDec = CustomButton("images/icon_minus.png")
        levelLayout.addWidget(self.btnLevelDec)