import deck
import players

def verification():
    #verification that the input is correct
    while (True):
        answer = input("Do you want to play? [y/n]: ")

        if (answer == "y" or answer == "n"):
            return answer
        else:
            print("Invalid data entry, please try again.")

def hit():
    #function for a hit in blackjack, using multiple classes
    return

def placeBet():
    pBet = 0
    pBet = int(input("Please enter your betting amount: "))
