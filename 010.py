import time
import math

start_time = time.time()

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes_sum = 0
max_num = 2_000_000
#for i in range(2, max_num):
 #   if is_prime(i):
  #      primes_sum += i

print(primes_sum)

print("Elapsed time: %s seconds" % (time.time() - start_time))

start_time = time.time()

sieve = {x: True for x in range(2, max_num)}
primes = list()

for i in range(2, int(math.sqrt(max_num))):
    if sieve[i]:
        for number in range(i, max_num, i):
            sieve[number] = False
        primes.append(i)

for number, status in sieve.items():
    if status:
        primes.append(number)

print(sum(primes))

print("Elapsed time: %s seconds" % (time.time() - start_time))
