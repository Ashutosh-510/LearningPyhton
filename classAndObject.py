class basket:
    # Mehtod
    def setfruit(self ,n ,c):
        self.name=n
        self.color=c
    def getfruit(self):
        print("object properties are: " , self.name , self.color)


    

object = basket()
m = basket()
basket.fruit(m ,"Mango" , "Yellow")
print(m.name , m.color)
object.fruit("Banana" , "Yellow")
#print(object.name , object.color)
object.getfruit()

