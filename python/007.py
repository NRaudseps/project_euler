def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = list()
for i in range(2, 150_000):
    if is_prime(i):
        prime_numbers.append(i)
        print(len(prime_numbers), i)

