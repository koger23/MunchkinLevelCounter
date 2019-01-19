from utils import DB_utils


class Player(object):

    def __init__(self, name=None):

        self.name = None
        if self.name:
            self.name = name
        self.rounds = 0
        self.wins = 0
        self.currentLevel = 1
        self.currentBonus = 0

    def setName(self, name):

        self.name = name

    def setRounds(self, rounds):

        self.rounds = rounds

    def setWins(self, wins):

        self.wins = wins

    def increaseLevel(self):

        self.currentLevel += 1

    def increaseBonus(self):

        self.currentBonus += 1

    def decreaseLevel(self):

        self.currentLevel -= 1

    def decreaseBonus(self):

        self.currentBonus -= 1

    def increaseWins(self):

        self.wins += 1

    def increaseRounds(self):

        self.rounds += 1

    def die(self):

        self.currentBonus = 0
        self.currentLevel = 1