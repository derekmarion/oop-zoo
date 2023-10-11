class Animal:
    def __init__(self, name, species) -> None:
        self._name = name
        self._species = species

    def speak(self, sound):
        return f"{sound}"
    
class Mammal(Animal):
    def __init__(self, name, species) -> None:
        super().__init__(name, species)

    def give_birth(self):
        print(f"{self._name} has given birth!")
    
class Bird(Animal):
    def __init__(self, name, species, wingspan) -> None:
        super().__init__(name, species="Bird")
        self._wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name, species) -> None:
        super().__init__(name, species)

    def bask_in_sun(self):
        print(f"{self._name} is basking in the sun")

class Primate(Mammal):
    def __init__(self, name, species) -> None:
        super().__init__(name, species)

    def climb_trees(self):
        print(f"{self._name} is climbing a tree!")

class Marsupial(Mammal):
    def __init__(self, name, species) -> None:
        super().__init__(name, species)

    def carry_baby(self):
        print(f"{self._name} is carrying its baby")

class Aviary():
    def __init__(self) -> None:
        self._birds = {}

class ReptileEnclosure():
    def __init__(self) -> None:
        self._reptiles = {}