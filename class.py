
# Design Your Own Class
class Shapes:
    def __init__(self, width, is_filled):
        self.width = width
        self.is_filled = is_filled

class Square(Shapes):
    def __init__(self, width, is_filled):
        super().__init__(width, is_filled)

    def area(self):
        return self.width * self.width

class Rectangle(Shapes):
    def __init__(self, width, is_filled, height):
        super().__init__(width, is_filled)
        self.height = height

    def area(self):
        return self.width * self.height

class Trapezium(Shapes):
    def __init__(self, width, is_filled, height, width2):
        super().__init__(width, is_filled)
        self.height = height
        self.width2 = width2

    def area(self):
        return 0.5 * (self.width + self.width2) * self.height 

square = Square(5, True)
rectangle = Rectangle(5, True, 6)
trapezium = Trapezium(5, True, 6, 7)

print(f'Square area: {square.area()}')
print(f'Rectangle area: {rectangle.area()}')
print(f'Trapezium area: {trapezium.area()}')



# Polymorphism Challenge
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):
    def speak(self):
        print("The cat MEOWS")

class Dog(Animal):
    def speak(self):
        print("The dog BARKS")

class Lion(Animal):
    def speak(self):
        print("The lion ROARS")

cat = Cat("Cat")
dog = Dog("Dog")
lion = Lion("Lion")

cat.speak()
cat.eat()
cat.sleep()

dog.speak()
dog.eat()
dog.sleep()

lion.speak()
lion.eat()
lion.sleep()