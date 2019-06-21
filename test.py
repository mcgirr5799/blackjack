import modules.deck as deck
import modules.players as players
import random


test = deck.CardDeck()

for i in range(53):
    print(test.drawCard())


    print("You drew a", test.deckCardTitles[test.cardName], "of", test.deckSuitTitles[test.suitName])
    print(i)
print(test.suitName)
print(test.cardName)
