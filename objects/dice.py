import random

class Dice(object):

    def __init__(self):

        self.value = 0

    def throw(self):

        self.value = random.randint(1, 6)
        print(self.value)
