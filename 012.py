from collections import Counter


def divisors_brute(n):
    numbers = list()

    for i in range(1, n + 1):
        if n % i == 0:
            numbers.append(i)

    return numbers


def divisors_fact(n):
    i = 2
    numbers = list()
    while n > 1:
        if n % i == 0:
            n /= i
            numbers.append(i)
        else:
            i += 1

    result = 1
    for k, v in Counter(numbers).items():
        result *= 1 + v

    return result


number = 0
for i in range(100000):
    divisor_count = divisors_fact(number)
    if divisor_count >= 500:
        print(divisor_count)
        print(number)
        break
    number += i
