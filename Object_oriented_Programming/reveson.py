class Car:
    # total car kitne bani hai check karna 
    total_car=0


    def __init__(self,brand,model):
        self.__brand=brand #Encapsulation means private value 
        self.__model=model
        Car.total_car+=1
     
    def get_brand(self):
        # Encapsulation topic
        return self.__brand + " This Is Our Brand "


    def fullname(self):
        return f'Car Brand Is {self.__brand} And Model Is {self.__model}'

    # polymorphism
    def fuel_type(self):
        return f'Diesel Or Petrol'


    @staticmethod
    def general_description():
        return 'Cars Are Good'

    @property
    def model(self):
        return self.__model


#inheritance 
class ElectronicCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def fuel_type(self):
        return f'Electric Charge'


# total car check kar raha hai
# print(Car.total_car)

# polymorphism
Innova=Car("Toyata","Innova")
# print(Innova.fuel_type())


# staticmethod
# my_car=Car("Toyata","Camry")
# print(my_car.general_description())
# print(Car.general_description())


# property decoration
fortuner=Car("Toyata","fortuner")
# fortuner.model="scorpio"
# print(fortuner.model)



myElectric=ElectronicCar("tesla","model s","80whv")
# print(myElectric.fuel_type())
# print(myElectric.brand)
# print(myElectric.get_brand())
# print(myElectric.model)
# print(myElectric.battery_size)
# print(myElectric.fullname())

# my_car=Car("Mahindra","Scorpio")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())