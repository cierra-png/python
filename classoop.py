class Gari:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading =0
    def describe_gari(self):
        return f"{self.model} {self.year} {self.make}"
    def read_odometer(self):
        return f"this car has {self.odometer_reading}"
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading