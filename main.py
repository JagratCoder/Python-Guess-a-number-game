import random
import sys

def game():
    print("*********The Perfect Guess*********")
    name = input("What is your Name : ")
    print("I am Thinking of a Number",name)
    print("Guess a Number Between 1 to 100")
    rNo = random.randint(1,100)
    guess = 1
    print(rNo)
    a = True

    while a:
        user = int(input("Guess the Number : "))
        # guess = guess + 1
        print(guess)
        if rNo > user:
            print("Your Guess is too Low!")
            guess = guess + 1
        
        elif rNo < user:
            print("Your Guess is too High!")
            guess = guess + 1

        else:
            print("Congratulations!,Your Guess is correct")
            print("You Guessed the Number in",guess,"times")
            # sys.exit()
            guess = guess
            again = input("Do you want to Play Again? (Yes or No) : ")
            if again == "Yes":
                a = True
            else:
                a = False

        with open("hiscore.txt","r") as f:
            text = f.read()
            data = int(text)
            hiscore = str(guess)

        if data > guess:
            with open("hiscore.txt",'w') as f:
                f.write(hiscore)
        elif data < guess:
            pass
        else:
            pass

game()