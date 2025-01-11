class Vehicle:
    def __init__(self, owner,model,color,engine_power):
        self.owner=owner
        self.__model=model
        self.__engine_power=engine_power
        self._color=color
        self.__COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def get_model(self):
        return self._Vehicle__model
    def get_horsepower(self):
        return self._Vehicle__engine_power
    def get_color(self):
        return self._color
    def print_info(self):
        print (f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")
    def set_color(self,new_color):
        self.new_color=new_color
        all_colors=self._Vehicle__COLOR_VARIANTS
        if self.new_color.lower() in all_colors:
            self._color=self.new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
