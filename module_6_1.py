# Задача "Съедобное, несъедобное"
class Animal:
    """
    alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
    """
    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
           print(f'{self.name} не стал есть {food.name}')
           self.alive = False

class Plant:
    """
    edible = False(съедобность), name - индивидуальное название каждого растения
    """
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name, edible = True):
        self.name = name
        self.edible = edible


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

