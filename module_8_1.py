def add_everything_up(number_1,number_2):
    try:
        summ_1=number_1+number_2
    except TypeError:
        return (f'{number_1}{number_2}')
    else:
        return (f'{round(summ_1,3)}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

