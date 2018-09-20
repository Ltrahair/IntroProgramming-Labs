#imports actual pie
import math
#CMPT 120L 113
#Fibonacci
#Author: Linus Trahair
#Date: 20th Sep 2018

def approxPi(n):
    den=1
    num=4
    res=0
    for i in range(n):
       

        if i%2==0:
           res+=num/den 
        else:
            res-=num/den
        
        den+=2
        
    return res


n=int(input("enter number of iterations for a series that approximates pi: "))

print("your approximation is "+str(approxPi(n)))
print("your approximation is "+str(abs(math.pi-approxPi(n)))+" off of what pi is")
