
class Product:
    def __init__(self,productName,productPrice,productQuantity):
        self.productName=productName
        self.productPrice=productPrice
        self.productQuantity=productQuantity
    def isThatMany(self,n):
        if n>self.productQuantity:
            return False
        else:
            return True
    def totalCost(self,n):
        return self.productPrice*n
    def removeProducts(self,n):
        self.productQuantity-=n


products= [Product("Ultrasonic range finder",2.50,4)
           ,Product("Servo motor",14.99,10)
           ,Product("Servo controller",44.95,5)
           ,Product("Microcontroller Board",34.95,7)
           ,Product("Laser range finder",149.99,2)
           ,Product("Lithium polymer battery",8.99,8)]



def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].productQuantity > 0:
            print(str(i)+")",products[i].productName, "$", products[i].productPrice)
    print()

    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        
        printStock()
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        
        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        count = int(vals[1])
        
        if products[prodId].isThatMany(count):
            if cash >= products[prodId].totalCost(count):
                products[prodId].removeProducts(count)
                cash -= products[prodId].totalCost(count)
                print("You purchased", count, products[prodId].productName+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].productName)
main()
