def is_prime(func):
    def wrapper(*args):
        n=func(*args)
        if n <= 1:
            print('Составное')
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print('Составное')
        print('Простое')
        return n
    return wrapper


@ is_prime
def sum_three(*args):
    summ_=sum(args)
    return summ_




result = sum_three(2, 3, 6)
print(result)
