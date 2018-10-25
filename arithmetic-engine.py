# CMPT 120 - Lab #6
# YOUR NAME
# DD-MMM-YYYY
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div','pow', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        if cmd =="quit":
            break
        elif not cmd=="add" and not cmd=="sub" and not cmd=="pow" and not cmd=="mult" and not cmd=="div":
            print("invalid command, use add, sub, mult, div, or quit.")
            continue
        else:
            
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except:
                print("the command you enterend was not valid try again\n")
                continue
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1 * num2
            elif cmd == "div":
                try:
                    result = num1 / num2
                except:
                    print("can't divide by zero\n")
                    continue
            elif cmd=="pow":
                result=num1**num2
               
            
        print("The result is " + str(result) + ".\n")
def main():
    showIntro()
    doLoop()
    showOutro()
main()
