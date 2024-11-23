numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes= [ ]
not_primes= [ ]
is_prime=True
k=0
for i in range(1,len(numbers)):
    a = numbers[i]
    if a <= 2:# Проверка не является ли число двойкой
        primes.append(numbers[i])
        continue
    else:
        for j in range(1,i):
             if numbers[i] % numbers[j]==0 :
                k=k+1
                continue
        if is_prime==(k<=0):
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
            k=0
print("Простые числа", primes)
print("Не простые числа", not_primes)
