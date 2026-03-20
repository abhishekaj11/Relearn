class Car(): 
 def __init__(self, brand, model, fuel_type):

        self.brand = brand 
        self.model = model
        self.fuel_type = fuel_type

cars = Car(brand="hyundai", model="verna", fuel_type="desel") 



cars.brand
cars.fuel_type
cars.model

print(f"Vehicle {cars.brand} {cars.model} is a {cars.fuel_type} car")
                                    