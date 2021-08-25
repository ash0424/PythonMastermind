# Mastermind Game Program

# For the computer to generate random colors
import random

# Introductory message
print("")
print("")
print(" $$\      $$\  $$$$$$\   $$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  $$\      $$\ $$$$$$\ $$\   $$\ $$$$$$$\   ")
print(" $$$\    $$$ |$$  __$$\ $$  __$$\|__$$  __|$$  _____|$$  __$$\ $$$\    $$$ |\_$$  _|$$$\  $$ |$$  __$$\  ")
print(" $$$$\  $$$$ |$$ /  $$ |$$ /  \__|  $$ |   $$ |      $$ |  $$ |$$$$\  $$$$ |  $$ |  $$$$\ $$ |$$ |  $$ | ")
print(" $$\$$\$$ $$ |$$$$$$$$ |\$$$$$$\    $$ |   $$$$$\    $$$$$$$  |$$\$$\$$ $$ |  $$ |  $$ $$\$$ |$$ |  $$ | ")
print(" $$ \$$$  $$ |$$  __$$ | \____$$\   $$ |   $$  __|   $$  __$$< $$ \$$$  $$ |  $$ |  $$ \$$$$ |$$ |  $$ | ")
print(" $$ |\$  /$$ |$$ |  $$ |$$\   $$ |  $$ |   $$ |      $$ |  $$ |$$ |\$  /$$ |  $$ |  $$ |\$$$ |$$ |  $$ | ")
print(" $$ | \_/ $$ |$$ |  $$ |\$$$$$$  |  $$ |   $$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |$$$$$$\ $$ | \$$ |$$$$$$$  | ")
print(" \__|     \__|\__|  \__| \______/   \__|   \________|\__|  \__|\__|     \__|\______|\__|  \__|\_______/  ")
print("")
print("")

# Game instructions
print("""\n"HOW TO PLAY"\n
        1. This game is between you and the computer.\n
        2. The computer will generate a random sequence of 4 colors that will not be displayed to you.\n
        3. You are supposed to guess the colors in the right order from a list of colors shown to you.\n
        4. You will be informed if you chose the correct color in the correct place, correct color in the
           wrong place or a color that is not used at all.\n
        5. You have 10 tries before the game asks you to start again.\n
        6. If you guess the color sequence correctly, you win!\n
        """)

# Input player name
# Create a list for player
player = []

# Define a function to make sure the player's name is already in the database
def add_player():
    global player


    def player_names():
        # Let player enter name
        global player1


        player1 = str(input("*PLAYER'S NAME?* ==> "))

        while True:
            while not player1:
                print("\nPLAYER 1 will not be added successfully\nPlease enter again.")
                player1 = str(input("*PLAYER'S NAME?* ==> "))
            while player1 == " ":
                print("\nPLAYER 1 will not be added successfully\nPlease enter again.")
                player1 = str(input("*PLAYER'S NAME?* ==> "))
            break



    player_names()

    player.append(player1)


    if player[0] == player1:
        print()
        print(player)
        print("Player is added successfully")


# Define function to select a block of code in order for it to perform a certain task (in this case to allow the player a restart option)
def main():


    myColorList = ['p', 'b', 'g', 'w', 'y', 'r'] # Colors used by the computer and player in the game

    # Each placement 1, 2, 3 and 4 will generate a random color for the computer from myColorList
    n1 = random.choice(myColorList)
    n2 = random.choice(myColorList)
    n3 = random.choice(myColorList)
    n4 = random.choice(myColorList)
    c = 1
    print("")
    print("""\nChoose from these Colors:\n
            'p' for purple\n
            'b' for blue\n
            'g' for green\n
            'w' for white\n
            'y' for yellow\n
            'r' for red\n
            """)

    x = 0
    for x in range(10): # For loop is used to automate the game and is set to a guess limit of 10 tries

        print("")
        if x+1 == 1:
            print("This will be your " + str(x + 1) + "st try.")
        elif x+1 == 2:
            print("This will be your " + str(x + 1) + "nd try.")
        elif x+1 == 3:
            print("This will be your " + str(x + 1) + "rd try.")
        else:
            print("This will be your " + str(x + 1) + "th try.")
            print("")
        print("You only have a maximum of 10 tries.")
        print("Or you lose and I win!")
        print("")
        # Player's input
        guess1 = input("Guess the first colour: ")
        guess2 = input("Guess the second colour: ")
        guess3 = input("Guess the third colour: ")
        guess4 = input("Guess the fourth colour: ")
        print("")
        x += 1
        numberswrong = 0 # Counts the player's wrong guesses in order to adhere to the guess limit

        if guess1 != n1:
            numberswrong += 1

        if guess2 != n2:
            numberswrong += 1

        if guess3 != n3:
            numberswrong += 1

        if guess4 != n4:
            numberswrong += 1

        if numberswrong == 0:
            print("")
            print('It is a Match !')
            print("Computer's answer : ", n1, ",", n2, ",", n3, ",", n4)
            print("")
            print("Well Done", player1, "!")
            if c == 1:
                print('It took you ' + str(c) + ' try to guess the colours.')

            elif c > 1:
                print('It took you ' + str(c) + ' tries to guess the colours.')
            print("")
            break
        else:
            print('Try Again!')
            print("")
        c += 1

        # If statements used to identify whether or not the player's guess matches the computer's color sequence
        i = 1
        if guess1 == n1:
            print("Guess 1: Correct color in the correct position!")
            i+=1
        elif guess1 == n2 or guess1 == n3 or guess1 == n4 :
            print("Guess 1: Correct color in the wrong position!")
        elif guess1 != n1 or guess1 != n2 or guess1 != n3 or guess1 != n4:
            print("Guess 1: This color is not used!")

        if guess2 == n2:
            print("Guess 2: Correct color in the correct position!")
            i+=1
        elif guess2 == n1 or guess2 == n3 or guess2 == n4 :
            print("Guess 2: Correct color in the wrong position!")
        elif guess2 != n1 or guess2 != n2 or guess2 != n3 or guess2 != n4:
            print("Guess 2: This color is not used!")

        if guess3 == n3:
            print("Guess 3: Correct color in the correct position!")
            i+=1
        elif guess3 == n1 or guess3 == n2 or guess3 == n4 :
            print("Guess 3: Correct color in the wrong position!")
        elif guess3 != n1 or guess3 != n2 or guess3 != n3 or guess3 != n4:
            print("Guess 3: This color is not used!")

        if guess4 == n4:
            print("Guess 4: Correct color in the correct position!")
            i+=1
        elif guess4 == n1 or guess4 == n2 or guess4 == n3 :
            print("Guess 4: Correct color in the wrong position!")
        elif guess4 != n1 or guess4 != n2 or guess4 != n3 or guess4 != n4:
            print("Guess 4: This color is not used!")

    if x == 10:
        print("")
        print("Game ended after 10 tries!")


    # While loop to prompt the player to restart the game or end it
    bool = True
    while bool:

        restart = input("Do you want to play again? (Y/N)")
        if restart == "Y" or restart == "y":
            main()
            bool = False
        elif restart == "N" or restart == "n":
            print("")
            print("Thanks for Playing!")
            bool = False
            exit()
        else:
            print("This is an invalid input.")
            bool = True


add_player()
main() # Wraps the selected block of code under define function (def main) signifying the end of the selected block
