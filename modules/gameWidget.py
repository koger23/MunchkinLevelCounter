from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QFrame
from PySide2.QtGui import QPixmap
from modules.customButtons import CustomButton
from PySide2.QtCore import Qt


class GameWidget(QWidget):


    def __init__(self, gameObj):
        super(GameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        mainLayout.setContentsMargins(10, 10, 0, 0)
        self.resize(600, 800)
        self.setMinimumWidth(600)
        self.setMaximumWidth(600)

        # Game object to count rounds
        self.game = gameObj

        # Round
        self.roundNumber = 1
        self.lblRounds = QLabel("Round " + str(self.game.rounds))
        self.lblRounds.setObjectName("RoundCounter")
        mainLayout.addWidget(self.lblRounds)
        self.lblRounds.setAlignment(Qt.AlignTop)
        self.lblRounds.setAlignment(Qt.AlignHCenter)

        # Picture fight
        lblPic = QLabel()
        pixMap = QPixmap("images/newGame.png")
        pixMap = pixMap.scaledToHeight(150, Qt.SmoothTransformation)
        lblPic.setPixmap(pixMap)
        mainLayout.addWidget(lblPic)
        lblPic.setAlignment(Qt.AlignTop)
        lblPic.setAlignment(Qt.AlignLeft)

        # Change gender
        lblGender = QLabel("Change sex")
        lblGender.setObjectName("lblGender")
        mainLayout.addWidget(lblGender)
        lblGender.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        lblGender = QLabel()
        pixMapGender = QPixmap("images/icon_changegender.png")
        pixMapGender = pixMapGender.scaledToHeight(100, Qt.SmoothTransformation)
        lblGender.setPixmap(pixMapGender)
        mainLayout.addWidget(lblGender)

        # Skull - dead
        lblSkull = QLabel("Die!")
        lblSkull.setObjectName("lblSkull")
        mainLayout.addWidget(lblSkull)
        lblSkull.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        lblSkull = QLabel()
        pixMapSkull = QPixmap("images/dead.png")
        pixMapSkull = pixMapSkull.scaledToHeight(100, Qt.SmoothTransformation)
        lblSkull.setPixmap(pixMapSkull)
        mainLayout.addWidget(lblSkull)
        lblSkull.setAlignment(Qt.AlignHCenter)

        # Dice
        lblThrow = QLabel("Throw")
        lblThrow.setObjectName("lblThrowDice")
        mainLayout.addWidget(lblThrow)
        lblThrow.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        lblDice = QLabel()
        pixMapDice = QPixmap("images/dice.png")
        pixMapDice = pixMapDice.scaledToHeight(50, Qt.SmoothTransformation)
        lblDice.setPixmap(pixMapDice)
        mainLayout.addWidget(lblDice)
        lblDice.setAlignment(Qt.AlignRight)

        # Counters
        counterLayout = QHBoxLayout()
        mainLayout.addLayout(counterLayout)

        self.bonusCounterWidget = BonusCountWidget()
        counterLayout.addWidget(self.bonusCounterWidget)

        self.levelCounterWidget = LevelCountWidget()
        counterLayout.addWidget(self.levelCounterWidget)

        # Placeholder
        lbl = QLabel()
        mainLayout.addWidget(lbl)

        # Next Player Button
        self.btnNextPlayer = QPushButton("Next Player")
        self.btnNextPlayer.setMinimumHeight(50)
        mainLayout.addWidget(self.btnNextPlayer)

    def increaseGameRounds(self):

        self.game.increaseRounds()
        self.lblRounds.setText(str(self.lblRounds))
        print(self.lblRounds)
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
        bonusLayout.addWidget(self.btnBonusInc, Qt.AlignHCenter)

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

class QHLine(QFrame):

    def __init__(self):

        super(QHLine, self).__init__()

        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)