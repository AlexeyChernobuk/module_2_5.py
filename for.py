numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    count_p = 0
    is_prime = bool
    if num >= 2:
        for j in range(1, num):
            p = num % j
            if p == 0 and j >= 1:
                count_p = count_p + 1
            else:
                count_p = count_p
        if count_p == 1:
            is_prime = True
        else:
            is_prime = False
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

print (f"Простые числа: {primes}")
print (f"Непростые числа: {not_primes}")