#CMPT 120L 113
#MadLibs
#Author: Linus Trahair
#Date: 6th Sep 2018

def promptForWords():
  global n,v,a,p
  n=input('Enter a noun: ')
  v=input('Enter a verb: ')
  a=input('Enter an adjective: ')
  p=input('Enter a place: ')

  
def makeAndPrintSentence():
  finalStr="The "+a+" "+n+" went "+v+" at the "+p
  print(finalStr)


def main():
  promptForWords()
  makeAndPrintSentence()
  #so it doesn't immediately exit when using terminal/powershell/command prompt
  input()

  
main()
