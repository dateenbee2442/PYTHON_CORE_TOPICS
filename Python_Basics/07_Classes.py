import converters

max = converters.kg_to_lbs(70)
print(max)

print(converters.lbs_to_kg(154.5))















class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking now')


old_man = Person('Ahmad')
old_man.talk()


class Mammal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name} walking....')



class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def bark(self):
        print(f'{self.name} is barking, Whooo Whooo')


class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def meow(self):
        print(f'{self.name} is meowwingggg')

dog = Dog('Luke')
dog.walk()
dog.bark()

cat1 = Cat('Pussy')
cat1.walk()
cat1.meow()


