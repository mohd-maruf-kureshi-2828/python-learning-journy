# class Protein:
#     def __init__(self,chicken,fish):
#         self.chicken=chicken
#         self.fish=fish


# protein=Protein(320,330)
# print(protein.chicken)
# print(protein.fish)


class Car:
    # total car count
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
  
    # Encapsulation
    def private_brand(self):
        return self.__brand
    
    
    def Car_Full_Details(self):
        return f"Call Full Name {self.brand} {self.model}"
    

    @staticmethod
    def general_description():
        return "Cars Are Good For High Ways"
    
    @property
    def model(self):
        return self.__model


    
    #polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    


class ELectric(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

       #polymorphism
    def fuel_type(self):
        return "ELectronic Charge"


# change nhi hoga q ke hum ne property decoration use kiye hai
santro=Car("hyunda","santro")
# santro.model="creta"
# print(santro.model)


santro=Car("hyunda","santro")
# print(santro.model())
# print(santro.fuel_type())

creta=Car("hyunda","santro")


# isinstance se hum dikhty hai car a object is car ka hai ya nhi hai tu tru diga nhi to false
my_electonic=ELectric("tesla","X",21700)
# print(isinstance(my_electonic,Car))
# print(isinstance(my_electonic,ELectric))


# print(my_electonic.fuel_type())
# print(my_electonic.Car_Full_Details())
# print(my_electonic.battery_size)
# print(my_electonic.brand)
# print(my_electonic.__brand) #Error
# print(my_electonic.private_brand())


# total car counting
# print(Car.total_car)

# print(Car.general_description())


# my_car=Car("Mahindra","scorpio")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.Car_Full_Details())



# my_new_car=Car("Toyota","corolla")
# print(my_new_car.brand)
# print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine"
class Electronic_1(Battery,Engine,Car):
    pass

my_frd_car=Electronic_1("tesla","model s")
print(my_frd_car.battery_info())
print(my_frd_car.engine_info())