import random

class CardDeck:

    def __init__(self):
        self.sizeLeft = 52

        #name for the chosen
        self.suitName = 0
        self.cardName = 0

        #4 arrays for each suit plus 13 elements in each to represent the card numbers
        self.deck = [[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]
        self.deckSuitTitles = {0:'Spades', 1:'Hearts', 2:'Clubs', 3:'Diamonds'}
        self.deckCardTitles = {0:'Ace', 1:'Two', 2:'Three', 3:'Four', 4:'Five', 5:'Six', 6:'Seven', 7:'Eight', 8:'Nine', 9:'Ten', 10:'Jack', 11:'Queen',12 :'King',}

    #modifications to the CardDeck
    def drawCard(self):
        exists = False
        emptyFlag = 0

        while (exists == False):
            rSuit = random.randint(0,3)
            self.suitName = rSuit

            rCard = random.randint(0,12)
            self.cardName = rCard
            chosenCard = self.deck[rSuit][rCard]

            if (chosenCard != 0):
                exists = True
                self.sizeLeft = self.sizeLeft - 1

                #sets the card to 0
                self.deck[rSuit][rCard] = 0
                return chosenCard

            #empty deck condition
            if (emptyFlag == 51):
                return None

            emptyFlag += 1
