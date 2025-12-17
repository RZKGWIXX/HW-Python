# class Animal:
#     def __init__(self, sound):
#         self._sound = sound
#     def sound(self):
#         return self._sound
# class Cat(Animal):
#     def __init__(self):
#         super().__init__("Meow")
#     def sound(self):
#         return super().sound()

# print(Cat().sound())

# class Shape:
#     def __init__(self, area):
#         self._area = area
#     def area(self):
#         self._area = 0
#         return self._area
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width * height)
#         self._width = width
#         self._height = height
#     def area(self):
#         self._area = self._width * self._height
#         return self._area
# rect = Rectangle(5, 4)
# print(rect.area())

# class Tramsport:
#     def __init__(self, speed):
#         self._speed = speed
#     def speed(self):
#         return self._speed
# class Car(Tramsport):
#     def __init__(self, speed):
#         super().__init__(speed)
#     def speed(self):
#         return super().speed()
# car = Car(120)
# print("Car speed:", car.speed())

# class Product:
#     def __init__ (self, name, price):
#         self._name = name
#         self._price = price

# class Food(Product):
#     def __init__ (self, name, price, expiration_date):
#         super().__init__(name, price)
#         self._expiration_date = expiration_date
#     def info(self):
#         return f"Food: {self._name}, Price: {self._price}$, Expiration Date: {self._expiration_date}"
# food_item = Food("Apple", 1.5, "2025-12-31")
# print(food_item.info())