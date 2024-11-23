numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes= [ ]
not_primes= [ ]
is_prime=True
for i in range(2,len(numbers)):
    a = numbers[i]
    for j in range(1,i+1):
        #a=numbers[i]
        b=numbers[j]
        if a % b==0 :
            not_primes.append(numbers[i])
        elif b!=a-1:
            continue

        break
numbers_set=set(numbers) # перевод во "множество"
not_primes_set=set(not_primes)# перевод во "множество"
primes=numbers_set-not_primes_set# вычитаем из общего списка не простые числа чтобы получить простые
primes.remove(1)# удаляю из множества простых чисел единицу, т.к. оно не простое число
print("Простые числа", primes)
print("Не простые числа", not_primes)
