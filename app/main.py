class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is True :
            self.hidden = False
        else :
            self.hidden = True


class Carnivore(Animal):

    def bite(self, animal: Animal | Herbivore | Carnivore) -> None:
        if isinstance(animal, Herbivore):
            if animal.hidden is not True:
                animal.health -= 50
            if animal.health <= 0:
                self.alive.remove(animal)
