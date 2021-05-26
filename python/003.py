def prime_factors(n):
    factors = list()
    i = 2

    while n > 2:
        if n % i == 0:
            n /= i
            factors.append(i)
            i = 2 
        else:
            i += 1

    return factors

number = input("Enter your number ")
print(prime_factors(int(number)))
