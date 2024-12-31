# Задача "Ошибка эволюции"

from random import randrange

class Animal:
    """
    класс описывающий животных
    """
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords[0] = self.speed * dx
        self._cords[1] = self.speed * dy
        if dz < 0:
            prnt("It's too deep, i can't dive :(")
        else:
            self._cords[2] = self.speed * dz
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)

class Bird(Animal):
    """
    класс описывающий птиц
    """
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randrange(1,4)} eggs for you")

class AquaticAnimal(Animal):
    """
    класс описывающий плавающего животного
    """
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - int(abs(dz) * self.speed / 2)

class PoisonousAnimal(Animal):
    """
    класс описывающий ядовитых животных
    """
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"
    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()