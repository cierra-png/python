class Fruit:

    def __init__(self, name, price):
        self.name=name
        self.price=price
    def onyesha(self):
        print(f"{self.name} is healthy for eating that costs at {self.price}")
myobj=Fruit("Apple","$20")
myobj.onyesha()
myobj1=Fruit("Mango","$12")
myobj1.onyesha()
myobj3=Fruit("Orange","$25")
myobj3.onyesha()
myobj4=Fruit("Pineapple","$35")
myobj4.onyesha()
myobj5=Fruit("Banana","$10")
myobj5.onyesha()
