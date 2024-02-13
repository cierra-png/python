class Car:

    def __init__(self, make, model, year, colour):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour
    def onyesha(self):
        print(f"My dream car is {self.make} and my model is "f"{self.model} manufactured in {self.year} and its {self.colour} in colour")
myobj=Car("Toyota","vitz",2020,"black")
myobj.onyesha()
myobj2=Car("Dodge", "challenger", "2019","purple")
myobj2.onyesha()