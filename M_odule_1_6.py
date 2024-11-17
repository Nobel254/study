my_dict={"Alex":1989,'lily':2000,'Viktor':1956}#создаю словарь
print("My dict",my_dict)#Вывод всего словаря
print("Год рождения Виктора: ",my_dict['Viktor'])# Вывод одного значения
print("Есть ли в словаре masha?",my_dict.get("masha","НЕТ"))
my_dict['John']=1968
my_dict['Oliver']=1980
print("Измененный словарь :", my_dict)#Вывод всего словаря
print("Год рождения Лилу : ", my_dict.pop("lily"))# удаление ключа "lily" и вывод его значения
print(my_dict)#Вывод всего словаря
print()
my_set={1,1,1,4,4,(43,3,66,6),6,"PAR",'Lola','PAR'}# Создаю множество
print("Изначальное множество: ",my_set)
my_set.add("Robin")
my_set.add((23,45))
print("Добавил два элемента ",my_set)
my_set.remove(6)
print("Удалил один элемент: ",my_set)


