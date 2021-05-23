def is_evenly_divisible(n):
    for i in range(1, 20):
        if n % i != 0:
            return False
    return True


for i in range(1_000_000_000):
    if is_evenly_divisible(i):
        print(i)
