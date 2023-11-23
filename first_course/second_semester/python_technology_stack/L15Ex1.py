#Есть родительский класс:
#class Transport:
#   def __init__(self, name, max_speed, mileage):
#self.name = name
#self.max_speed = max_speed
#self.mileage = mileage
#Создайте объект Autobus, который унаследует все переменные 
#и методы родительского класса Transport и выведете его.
#Ожидаемый результат вывода:
#Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

autobus = Autobus("Renault Logan", 180, 12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")
