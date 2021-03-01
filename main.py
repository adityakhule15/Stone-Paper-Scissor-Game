import random
# Importing Random for generating random veriable
import emoji
# Importing emoji for printing emoji with massege
def gameWin(comp, you):

    if comp==you:
        return None

    # Check for all possibilities when computer chose Stone
    elif comp == 's':
        if you=='c':
            return False
        elif you=='p':
            return True
    
    # Check for all possibilities when computer chose Paper
    elif comp == 'p':
        if you=='c':
            return True
        elif you=='s':
            return False
    
    # Check for all possibilities when computer chose Scissors
    elif comp == 'c':
        if you=='p':
            return False
        elif you=='s':
            return True

print("Comp Turn: Stone(s) Paper(p) or Scissors(c)?")
randNo = random.randint(1, 3) 
# Generating random no. between 1 to 3
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'c'

you = input("Your Turn: Stone(s) Paper(p) or Scissors(c)?\n")
a = gameWin(comp, you)

if comp == 's':
    print("Computer chose Stone")
elif comp == 'p':
    print("Computer chose Paper")
else:
    print("Computer chose Scissors")


if you == 's':
    print("You chose Stone")
elif you == 'p':
    print("You chose Paper")
else:
    print("You chose Scissors")

if a == None:
    print("The game is a tie!", end=" ")
    print(emoji.emojize(":winking_face_with_tongue:"))
elif a:
    print("You Win!", end=" ")
    print("\U0001F970")
else:
    print("You Lose!", end=" ")
    print(emoji.emojize(":zipper-mouth_face:")) 
