#CMPT 120L 113
#Author: Linus Trahair
#Mars Rover program
#purpose: to calculate time that is needed to send a picture from mars
#Date: 6 Sep 2018

#converts distance to time
def calcTime(dist):
    x=186000
    tm=dist/x
    return tm
#prints the result
print("time it takes is",calcTime(34000000),"seconds")
