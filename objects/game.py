

class Game(object):

    def __init__(self):
        super(Game, self).__init__()

        self.rounds = 1

    def increaseRounds(self):

        self.rounds += 1
        print(self.rounds)