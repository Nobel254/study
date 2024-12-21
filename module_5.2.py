class House:
    def __init__(self,name_course,number):
        self.name=name_course
        self.number_of_floors=number
    def go_to(self,new_floor):
        if new_floor>self.number_of_floors or new_floor<1:
            print("Такого этажа не существует")
        else:
            for x in range(new_floor):
                print(x + 1)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))