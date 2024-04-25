class Animal:
    def make_sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

class Farm:
    def __init__(self, animals):
        self.animals = animals

    def animal_sounds(self):
        sounds = []
        for animal in self.animals:
            sounds.append(animal.make_sound())
        return sounds

dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]
my_farm = Farm(animals)

animal_sounds = my_farm.animal_sounds()
for sound in animal_sounds:
    print(sound)