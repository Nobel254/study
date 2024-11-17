grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron',}

string_students=(list(students))#преводим в список
sort_students=sorted(string_students)#сортируем студентов по алфавиту

grades_avg=[]#Заполняею строку средними значениями
index = 0
while index < len(grades):
    grades_avg.append(sum(grades[index])/len(grades[index]))
    index += 1

dictionary=dict(zip(sort_students, grades_avg))#заполняю словарь

print(dictionary)








