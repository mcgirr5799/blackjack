import modules.deck as deck
import modules.players as players
import modules.features as features
import random

#loop variables
wantToPlay = "y"
#introductions
print("""
Welcome to Blackjack!

Creator: Shawn McGirr

This is a really shitty project but I'll try my best to keep practicing.
""")

while (True):
    if (features.verification() == "y"):
        print("Alright let us being")

        #initialize player and dealer
        user = players.Players()
        dealer = players.Players()
    else:
        print("Thanks it was fun playing with you <3")
        break
