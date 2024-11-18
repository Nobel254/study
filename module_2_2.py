first=input("Введите первое число : ",)
second =input("Введите второе число : ",)
third=input("Введите третье число : ",)
if first!=second and second!=third and first!=third :
    print("Количество введенных равных чисел : ", 0)
elif first==second and second==third:
    print("Количество введенных равных чисел : ", 3)
else:print("Количество введенных равных чисел : ", 2)
