#CMPT 120L 113
#Fibonacci
#Author: Linus Trahair
#Date: 20th Sep 2018


#for calculating the sequence
def sequence(n):
    #the variable to be outputed
    prevf=0

    #is the most current variable
    f=1
    
    #variable for storing the previous value of the most current variable to be added to prevf
    holdVar=0
    for i in range(0,n):
        holdVar=f
        f+=prevf
        prevf=holdVar
       
    return prevf


#checks if the program works
n=input("enter number of sequence in the Fibonacci sequence: ")
print(sequence(int(n)))
