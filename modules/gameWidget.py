from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PySide2.QtGui import QIcon, QFontDatabase
from modules.customButtons import CustomButton


class GameWidget(QWidget):


    def __init__(self):
        super(GameWidget, self).__init__()

        centralWidget = QWidget()
        mainLayout = QVBoxLayout(centralWidget)
        self.setLayout(mainLayout)
        self.setMaximumHeight(400)

        buttonsLayout = QHBoxLayout()
        mainLayout.addLayout(buttonsLayout)

        bonusLayout = QVBoxLayout()
        buttonsLayout.addLayout(bonusLayout)
        levelLayout = QVBoxLayout()
        buttonsLayout.addLayout(levelLayout)

        # Bonus buttons and label
        self.btnBonusDec = CustomButton("images/icon_minus.png")
        bonusLayout.addWidget(self.btnBonusDec)

        lblBonus = QLabel("Bonus")
        lblBonus.setObjectName("bonusLabel")
        bonusLayout.addWidget(lblBonus)

        self.btnBonusInc = CustomButton("images/icon_plus.png")
        bonusLayout.addWidget(self.btnBonusInc)

        self.btnLevelDec = CustomButton("images/icon_minus.png")
        levelLayout.addWidget(self.btnLevelDec)

        lblLevel = QLabel("Level")
        lblLevel.setObjectName("bonusLabel")
        levelLayout.addWidget(lblLevel)

        self.btnLevelInc = CustomButton("images/icon_plus.png")
        levelLayout.addWidget(self.btnLevelInc)


