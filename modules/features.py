def verification():
    #verification that the input is correct
    while (True):
        answer = input("Do you want to play? [y/n]: ")

        if (answer == "y" or answer == "n"):
            return answer
        else:
            print("Invalid data entry, please try again.")
