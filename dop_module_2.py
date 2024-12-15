password=''
para=[]
random_number=int(input('Введите число от 3 до 20 :'))
if 3>random_number or random_number>20:
    print('Вы ввели не правильное число')
else:
    for i in range(1,random_number):
        for j in range(i+1,random_number):
            a = i + j
            b=random_number % a
            if  b==0:
                password+=f"{i}{j}"
    print(f'Password : {password}')
