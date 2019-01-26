from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PySide2.QtGui import QPixmap
from objects import dice
from modules.customButtons import CustomButton
from PySide2.QtCore import Qt, QTime
import time


class GameWidget(QWidget):


    def __init__(self, gameObj):
        super(GameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        mainLayout.setContentsMargins(20, 0, 0, 0)
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

        # Time elapsed label
        self.startTime = time.time()
        self.endTime = time.time()
        self.lblTime = QLabel('00:00:00')
        self.lblTime.setObjectName("lblElapsedTime")
        roundsLayout.addWidget(self.lblTime)
        self.lblTime.setAlignment(Qt.AlignCenter)

        # Picture fight
        self.lblPic = QLabel()
        pixMap = QPixmap("images/newGame-" + str(self.game.rounds) + ".png")
        pixMap = pixMap.scaledToHeight(200, Qt.SmoothTransformation)
        self.lblPic.setPixmap(pixMap)
        roundsLayout.addWidget(self.lblPic)
        self.lblPic.setAlignment(Qt.AlignCenter)

        # Change gender
        lblGender = QLabel()
        pixMapGender = QPixmap("images/icon_changegender.png")
        pixMapGender = pixMapGender.scaledToHeight(100, Qt.SmoothTransformation)
        lblGender.setPixmap(pixMapGender)
        genderLayout.addWidget(lblGender)
        lblGender.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

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
        lblSkull.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.btnDie = QPushButton("Die!")
        self.btnDie.setObjectName("gameIconBtn")
        dieLayout.addWidget(self.btnDie)
        self.btnDie.setMaximumWidth(120)

        # Dice
        self.dice = dice.Dice()

        self.lblDice = QLabel()
        pixMapDice = QPixmap("images/dice.png")
        pixMapDice = pixMapDice.scaledToHeight(80, Qt.SmoothTransformation)
        self.lblDice.setPixmap(pixMapDice)
        diceLayout.addWidget(self.lblDice)
        self.lblDice.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.btnThrow = QPushButton("Throw")
        self.btnThrow.setObjectName("gameIconBtn")
        diceLayout.addWidget(self.btnThrow)
        self.btnThrow.setMaximumWidth(120)

        mainLayout.addSpacing(70)

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

        if maxPlayerLevel % 10 == 0:
            pixMapRaw = QPixmap("images/newGame-10.png")
            pixMap = pixMapRaw.scaledToHeight(200, Qt.SmoothTransformation)
        else:
            pixMapRaw = QPixmap("images/newGame-" + str(maxPlayerLevel)[-1:] + ".png")
            pixMap = pixMapRaw.scaledToHeight(200, Qt.SmoothTransformation)

        self.lblPic.setPixmap(pixMap)
        self.lblPic.repaint()

    def increaseGameRounds(self):

        self.game.increaseRounds()
        self.lblRounds.setText(str(self.lblRounds))
        self.repaint()

    def timeWorker(self):

        """
        Updateting elapsed time.
        """

        timer = QTime()
        timer.start()
        self.breaker = 0

        while self.breaker != 1:
            time.sleep(1)

            m, s = divmod(timer.elapsed()//1000, 60)
            h, m = divmod(m, 60)
            self.lblTime.setText("%d:%02d:%02d" % (h, m, s))

    def changeDicePic(self):

        val = self.dice.throw()
        pixMapDice = QPixmap("images/dice-" + str(val) + ".png")
        pixMapDice = pixMapDice.scaledToHeight(80, Qt.SmoothTransformation)
        self.lblDice.setPixmap(pixMapDice)

        time.sleep(3)

        pixMapDice = QPixmap("images/dice.png")
        pixMapDice = pixMapDice.scaledToHeight(80, Qt.SmoothTransformation)
        self.lblDice.setPixmap(pixMapDice)

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