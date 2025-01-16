def personal_sum(numbers):
    incorrect_data=0
    result=0
    for number in numbers:
        try:
            result+=number
        except TypeError:
            incorrect_data+=1
            print('Некорректный тип данных для подсчёта суммы',number)
    return (result,incorrect_data)

def calculate_average(numbers):
    count=0
    try:
        summ1=personal_sum(numbers)
        for number in numbers:
            if type(number)==int or type(number)==float:
                count+=1
        average=summ1[0]/count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return
    return average

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать