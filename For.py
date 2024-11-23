numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

while numbers (n**0.5+1) :

    is_primes = True
    if numbers % numbers== 0:
            is_primes = False
    if is_primes:
        primes.append(numbers)
    else:
        not_primes.append(numbers)

print("Primes:", primes)
print("Not Primes:", not_primes)
