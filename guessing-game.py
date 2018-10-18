#Author: Linus Trahair
#Created: 18th Oct 2018
#Guessing game
#CMPT 120L

print("Guessing Game")
answer="penguin"

while True:
    print("\n I am thinking of some type of animal")
    Pans=input("\n Guess what I am thinking:\n").lower()
    if Pans==answer:
        print("you won!")
       
        while True:
             Pans=input("do you like this animal?(y/n)\n")
             if Pans[0]=="y":
                print("yay!")
                break
             elif Pans[0]=="n":
                print(";(")
                break
             else:
                print("invalid response")
            
        break
    elif Pans[0]=="q":
        break
    else:
        print("nope I was thinking of a different animal\n")
