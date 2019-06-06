class Players:
    #superclass
    def __init__(self, x = 100, y = 0):
        self.balance = x
        self.hand = y
        self.bet = 0

    #players hand methods
    def printHand(self):
        return self.hand

    def modifyHand(self, x):
        self.hand += x

    def resetHand(self):
        self.hand = 0

    #player betting methods
    def printbet(self):
        return self.bet

    def modifybet(self, x):
        self.bet += x

    def resetbet(self):
        self.bet = 0
