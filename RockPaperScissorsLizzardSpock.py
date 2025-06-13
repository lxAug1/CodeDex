import random

print("===================")
print("Rock Paper Scissors Lizzard Spock")
print("===================")
print("    1.Rock")
print("    2.Paper")
print("    3.Scissors")
print("    4.Lizzard")
print("    5.Spock")
playerOption = int(input("Pick a number: "))

computer = random.randint(1,5)

print("You selected:", playerOption)

print("The computer selected: ", computer)

#When the player win
if (playerOption == 1 and computer == 3):
    print("You won! Rock breaks Scissors.")
elif (playerOption == 2 and computer == 1):
    print("You won! Paper covers Rock.")
elif (playerOption == 3 and computer == 2):
    print("You won! Scissors cut Paper.")
elif(playerOption == 1 and computer == 4):
    print("You won! Rock crushes Lizard.")
elif (playerOption == 4 and computer == 5):
    print("You won! Lizard poisons Spock.")
elif (playerOption == 5 and computer == 3):
    print("You won! Spock smashes Scissors.")
elif (playerOption == 3 and computer == 4):
    print("You won! Scissors beat Lizard.")
elif (playerOption == 4 and computer == 2):
    print("You won! Lizard eats Paper.")
elif (playerOption == 2 and computer == 5):
    print("You won! Paper disproves Spock.")
elif (playerOption == 5 and computer == 1):
    print("You won! Spock vaporizes Rock.")
    
#When the computer win

if (playerOption == 3 and computer == 1):
    print("You lost! Rock breaks Scissors.")
elif (playerOption == 1 and computer == 2):
    print("You lost! Paper covers Rock.")
elif (playerOption == 2 and computer == 3):
    print("You lost! Scissors cut Paper.")
elif(playerOption == 4 and computer == 1):
    print("You lost! Rock crushes Lizard.")
elif (playerOption == 5 and computer == 4):
    print("You lost! Lizard poisons Spock.")
elif (playerOption == 3 and computer == 5):
    print("You lost! Spock smashes Scissors.")
elif (playerOption == 4 and computer == 3):
    print("You lost! Scissors beat Lizard.")
elif (playerOption == 2 and computer == 4):
    print("You lost! Lizard eats Paper.")
elif (playerOption == 5 and computer == 2):
    print("You lost! Paper disproves Spock.")
elif (playerOption == 5 and computer == 1):
    print("You lost! Spock vaporizes Rock.")
    
#When both sides choose the same thing

if (computer == 1 and playerOption == 1):
    print("No one win! Both sides selected the same thing.")
elif (computer == 2 and playerOption == 2):
    print("No one win! Both sides selected the same thing.")
elif (computer == 3 and playerOption == 3):
    print("No one win! Both sides selected the same thing.")
elif (computer == 4 and playerOption == 4):
    print("No one win! Both sides selected the same thing.")
elif (computer == 5 and playerOption == 5):
    print("No one win! Both sides selected the same thing.")
