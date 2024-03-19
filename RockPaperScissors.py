import random

print("***Rock-Paper-Scissor Game***")
Quit=""
myList = ['r','p','s']
while Quit!="q":
    Choice=""
    while Choice not in myList:
        Choice = input("Please enter your choice:\nr = Rock\np = Paper\ns = Scissor\n").lower()

    Compoterchoice=random.choice(myList)

    print("Your choice: ",Choice)
    print("Computer's choice: ",Compoterchoice)

    if Compoterchoice==Choice:
        print("No winner.")
    elif (Compoterchoice=='r' and Choice=='s')or(Compoterchoice=='p'and Choice=='r')or(Compoterchoice=='s'and Choice=='p'):
        print("Computer won.")
    else:
        print("YOU WON!!!")

    Quit=input("If you want to quit, press q. If not, press another letter:").lower()

print("Thanks for visiting:)")
