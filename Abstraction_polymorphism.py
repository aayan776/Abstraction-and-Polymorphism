from abc import ABC, abstractmethod
class test1(ABC):
    def print(self, x):
        print(f"Passed value: {x}")
    @abstractmethod
    def task(self):
        print("We are inside an abstract class.")
class test2(test1):
    def task(self):
        print("We are inside test2 class.")
obj1 = test2()
obj1.task()
obj1.print(1000000)
#Animal class
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can run and walk!")
class Snake(Animal):
    def move(self):
        print("I can crawl!")
class Bird(Animal):
    def move(self):
        print("I can fly!")
class Fish(Animal):
    def move(self):
        print("I can swim!")
H = Human()
H.move()
S = Snake()
S.move()
B = Bird()
B.move()
F = Fish()
F.move()

class India():
    def capital(self):
        print("My capital is New Delhi.")
    def language(self):
        print("The most spoken language in my country is Hindi.")
    def type(self):
        print("India is still developing.")
class USA():
    def capital(self):
        print("My capital is Washington D.C.")
    def language(self):
        print("The most spoken language in my country is English.")
    def type(self):
        print("USA is a developed country.")
ind = India()
us = USA()
for country in (ind, us):
    country.capital()
    country.language()
    country.type()