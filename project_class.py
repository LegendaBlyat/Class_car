class Car:
    brand = None
    model = None
    year = None
    mileage = None
    engine_started = False
    fuel_level = None

    def cars(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def drive (self, mileage ):
        self.mileage = mileage



    def display_info(self):
        print(self.brand, self.model, 'Age:', self.year, 'mileage:',
              self.mileage, 'km,', 'engine_started:', self.engine_started)

    # def __init__(self):
    #     self.fuel_level =
    def refuel(self, amount):
        if amount > 100:
            print('Бак переполнен')
        else:
            self.fuel_level = amount

    def get_fuel_level(self):
        print(self.fuel_level)



car1=Car()
car1.cars(brand='Nissan', model='GT-R,', year=2020,
                   mileage=150)
car2=Car()
car2.cars(brand='Lada', model='Vesta,', year=2005,
          mileage=13000)
car3=Car()
car3.cars(brand='Tayota', model='Corolla,', year=2008,
          mileage=3600)

car1.start_engine()
car1.display_info()
car1.refuel(0)
car2.start_engine()
car2.display_info()
car2.refuel(0)
car3.start_engine()
car3.display_info()
car3.refuel(0)




