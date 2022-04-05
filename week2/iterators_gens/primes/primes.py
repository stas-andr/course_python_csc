import itertools

from math import sqrt

def primes():
    prime = 2
    while True:
        while True:
            has_delims = False
            for i in range(2, int(sqrt(prime)) + 1):
                if prime % i == 0:
                    has_delims = True
                    break
            if not has_delims:
                break
            prime += 1
        yield prime
        prime += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]