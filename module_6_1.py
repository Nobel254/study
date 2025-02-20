class  Animal:
    def __init__(self,name,alive = True,fed = False):
        self.name=name
        self.alive=alive
        self.fed=fed
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed= True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive= False

class Mammal(Animal):
    Animal.alive = True
class Predator(Animal):
    Animal.alive = True
class  Plant:
    edible = False
class Flower(Plant):
    edible = False
    def __init__(self,flower):
         self.name=flower
class Fruit (Plant):
    edible = True
    def __init__(self,fruit):
         self.name=fruit
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
