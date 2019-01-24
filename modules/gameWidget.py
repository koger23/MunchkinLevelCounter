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

        # create Layouts
        roundsLayout = QVBoxLayout()
        mainLayout.addLayout(roundsLayout)

        iconsLayout = QHBoxLayout()
        mainLayout.addLayout(iconsLayout)

        genderLayout = QVBoxLayout()
        iconsLayout.addLayout(genderLayout)

        dieLayout = QVBoxLayout()
        iconsLayout.addLayout(dieLayout)

        diceLayout = QVBoxLayout()
        iconsLayout.addLayout(diceLayout)

        # Game object to count rounds
        self.game = gameObj

        # Round
        self.roundNumber = 1
        self.lblRounds = QLabel("Round " + str(self.game.rounds))
        self.lblRounds.setObjectName("RoundCounter")
        roundsLayout.addWidget(self.lblRounds)
        self.lblRounds.setAlignment(Qt.AlignCenter)

        # Picture fight
        self.lblPic = QLabel()
        pixMap = QPixmap("images/newGame-" + str(self.game.rounds) + ".png")
        pixMap = pixMap.scaledToHeight(200, Qt.SmoothTransformation)
        self.lblPic.setPixmap(pixMap)
        roundsLayout.addWidget(self.lblPic)
        self.lblPic.setAlignment(Qt.AlignCenter)

        mainLayout.addSpacing(50)

        # Change gender
        lblGender = QLabel()
        pixMapGender = QPixmap("images/icon_changegender.png")
        pixMapGender = pixMapGender.scaledToHeight(100, Qt.SmoothTransformation)
        lblGender.setPixmap(pixMapGender)
        genderLayout.addWidget(lblGender)
        lblGender.setAlignment(Qt.AlignCenter)

        self.btnGender = QPushButton("Change Sex")
        self.btnGender.setObjectName("gameIconBtn")
        genderLayout.addWidget(self.btnGender)
        self.btnGender.setMaximumWidth(120)

        # Skull - dead
        lblSkull = QLabel()
        pixMapSkull = QPixmap("images/dead.png")
        pixMapSkull = pixMapSkull.scaledToHeight(100, Qt.SmoothTransformation)
        lblSkull.setPixmap(pixMapSkull)
        dieLayout.addWidget(lblSkull)
        lblSkull.setAlignment(Qt.AlignCenter)

        self.btnDie = QPushButton("Die!")
        self.btnDie.setObjectName("gameIconBtn")
        dieLayout.addWidget(self.btnDie)
        self.btnDie.setMaximumWidth(120)

        # Dice
        lblDice = QLabel()
        pixMapDice = QPixmap("images/dice.png")
        pixMapDice = pixMapDice.scaledToHeight(80, Qt.SmoothTransformation)
        lblDice.setPixmap(pixMapDice)
        lblDice.setAlignment(Qt.AlignCenter)
        diceLayout.addWidget(lblDice)

        btnThrow = QPushButton("Throw")
        btnThrow.setObjectName("gameIconBtn")
        diceLayout.addWidget(btnThrow)
        btnThrow.setMaximumWidth(120)

        # Counters
        counterLayout = QHBoxLayout()
        mainLayout.addLayout(counterLayout)

        self.bonusCounterWidget = BonusCountWidget()
        counterLayout.addWidget(self.bonusCounterWidget)

        self.levelCounterWidget = LevelCountWidget()
        counterLayout.addWidget(self.levelCounterWidget)

        mainLayout.addSpacing(50)

        # Next Player Button
        self.btnNextPlayer = QPushButton("Next Player")
        self.btnNextPlayer.setMinimumHeight(50)
        mainLayout.addWidget(self.btnNextPlayer)

    def changeGamePic(self, maxPlayerLevel):

        pixMapRaw = QPixmap("images/newGame-" + str(maxPlayerLevel) + ".png")
        pixMap = pixMapRaw.scaledToHeight(200, Qt.SmoothTransformation)
        self.lblPic.setPixmap(pixMap)
        self.lblPic.repaint()

    def increaseGameRounds(self):

        self.game.increaseRounds()
        self.lblRounds.setText(str(self.lblRounds))
        print(self.lblRounds)
        self.repaint()

    def test(self):
        print("Print")


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
        bonusLayout.addWidget(self.btnBonusInc, 0, Qt.AlignHCenter)

        lblBonus = QLabel("<Bonus>")
        lblBonus.setAlignment(Qt.AlignHCenter)
        lblBonus.setObjectName("bonusLabel")
        bonusLayout.addWidget(lblBonus)

        self.btnBonusDec = CustomButton("images/icon_minus.png")
        bonusLayout.addWidget(self.btnBonusDec, 0, Qt.AlignHCenter)


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
        levelLayout.addWidget(self.btnLevelInc, 0, Qt.AlignHCenter)

        lblLevel = QLabel("<Level>")
        lblLevel.setAlignment(Qt.AlignHCenter)
        lblLevel.setObjectName("bonusLabel")
        levelLayout.addWidget(lblLevel)

        self.btnLevelDec = CustomButton("images/icon_minus.png")
        levelLayout.addWidget(self.btnLevelDec, 0, Qt.AlignHCenter)

class QHLine(QFrame):

    def __init__(self):

        super(QHLine, self).__init__()

        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)