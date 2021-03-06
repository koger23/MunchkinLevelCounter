from utils import DB_utils as dbu
import os


class Player(object):

    def __init__(self, name):

        self.name = name
        self.games = 0
        self.wins = 0
        self.currentLevel = 1
        self.currentBonus = 0
        self.gender = "male"
        self.avatar = r"\images\munchkin_" + self.gender + ".png"
        self.inGame = 0
        self.id = None
        self.isAlive = 1
        self.rounds = 1
        self.winner = False

        if self.isAlive == 0:
            self.avatar = r"\images\dead.png"
        else:
            r"\images\munchkin_" + self.gender + ".png"

        self.setId()

    def setRounds(self, rounds):

        self.rounds = rounds

    def setId(self):


        self.id = dbu.Database().getPlayerId(self.name, self.games, self.wins)
        if self.id:
            self.id = self.id[0][0]


    def setName(self, name):

        self.name = name

    def setGames(self, rounds):

        self.games = rounds

    def setWins(self, wins):

        self.wins = wins

    def setGender(self, gender):

        if gender == "male" or gender == "female" or gender == "neutral":
            self.gender = gender
        else:
            self.gender = "male"

    def setAvatar(self, path=None):

        if path:
            self.avatar = path
        else:
            defaultPath = os.path.realpath(__file__).replace("\objects\players.py", "/images")
            imageName = "munchkin_" + self.gender + ".png"
            self.avatar = os.path.join(defaultPath, imageName)

    def increaseRounds(self):

        self.rounds += 1

    def increaseLevel(self):

        self.currentLevel += 1

        if self.currentLevel > 10:
            self.currentLevel = 10

        if self.currentLevel == 10 and self.winner is False:
            self.wins += 1
            self.winner = True
            self.saveWin()

    def increaseBonus(self):

        self.currentBonus += 1

    def decreaseLevel(self):

        self.currentLevel -= 1

        if self.currentLevel < 1:
            self.currentLevel = 1

    def decreaseBonus(self):

        self.currentBonus -= 1
        if self.currentBonus < 0:
            self.currentBonus = 0

    def changeGender(self):

        if self.gender == 'male':
            self.gender = 'female'
        elif self.gender == 'female':
            self.gender = 'neutral'
        else:
            self.gender = 'male'
        self.setAvatar()

    def increaseWins(self):

        self.wins += 1

    def saveWin(self):

        dbu.Database().update(self.id, self.name, self.games, self.wins, self.rounds)


    def die(self):

        self.currentBonus = 0
        # self.isAlive = 0
        # self.avatar = r"Y:\Dropbox\Python\MunchkinLevelCounter\images\munchkin\dead.png"