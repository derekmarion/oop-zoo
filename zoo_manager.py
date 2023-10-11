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
    
