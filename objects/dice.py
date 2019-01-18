import random

class Dice(object):

    def __init__(self):

        self.value = 0

    def drop(self):

        self.value = random.randint(0, 6)
