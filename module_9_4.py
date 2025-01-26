'''Lambda-функция'''
first = 'Мама мыла раму'
second = 'Рамена мало было'
sovpad=lambda x,y:x==y
print(list(map(sovpad, first, second)))

'''Замыкание:'''
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name,"w") as file:
            for i in range(len(data_set)):
                file.write(f'{data_set[i]}\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

'''Метод __call__'''
from random import choice
class MysticBall:
    def __init__(self,*words):
        self.words=words
    def __call__(self):
        random_word= choice(self.words)
        return random_word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
