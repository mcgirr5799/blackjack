import random

class CardDeck:

    def __init__(self):
        self.sizeLeft = 52
        #4 arrays for each suit plus 13 elements in each to represent the card numbers
        self.deck = [[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]
        self.deckNumbersTitles = {1: 'Spades', 2:'Hearts', 3: 'Clubs', 4:'Diamonds'}

    #modifications to the CardDeck
    def drawCard(self):
        exists = False
        while (exists == False):
            rSuit = random.randint(0,3)
            rCard = random.randint(0,12)
            chosenCard = self.deck[rSuit][rCard]

            if (chosenCard != 0):
                exists = True
                self.sizeLeft = self.sizeLeft - 1

                #sets the card to 0
                self.deck[rSuit][rCard] = 0
                return chosenCard
