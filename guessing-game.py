#Author: Linus Trahair
#Created: 18th Oct 2018
#Guessing game
#CMPT 120L

print("Guessing Game")
answer="penguin"

while True:
    print("\n I am thinking of some type of animal")
    Pans=input("\n Guess what I am thinking:\n")
    if Pans==answer:
        print("you won!")
        break
    else:
        print("nope I was thinking of a different animal\n")
