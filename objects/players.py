from utils import DB_utils


class Player(object):

    def __init__(self):

        self.name = None
        self.rounds = 0
        self.wins = 0
        self.currentLevel = 0
        self.currentCloth = 0

    def setName(self, name):

        self.name = name

    def increaseLevel(self):

        self.currentLevel += 1

    def increaseCloth(self):

        self.currentCloth += 1

    def decreaseLevel(self):

        self.currentLevel -= 1

    def decreaseCloth(self):

        self.currentCloth -= 1

    def increaseWins(self):

        self.wins += 1

    def increaseRounds(self):

        self.rounds += 1

    def die(self):

        self.currentCloth = 0
        self.currentLevel = 1