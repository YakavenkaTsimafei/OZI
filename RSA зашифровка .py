import math
from random import random, randint


def prime(number):
    z = number
    counter = 0
    for i in range(1, z + 1):
        if z % i == 0:
            counter += 1
    return True if counter == 2 else False


messageForEncryption = int(input())

while True:
    q = randint(0, 1000)
    p = randint(0, 1000)
    if q * p > messageForEncryption and math.gcd(p, q) == 1 and prime(p) == True and prime(q) == True:
        break
n = q * p
f = (p - 1) * (q - 1)
while True:
    e = randint(0, 1000)
    if math.gcd(e, f) == 1:
        break
print(f"p = {p}")
print(f"q = {q}")
print(f"e = {e}")
print(f"f = {f}")
print(f"n = {n}")
answer = messageForEncryption ** e % n
print(f"encrypted message : ({answer},{e},{n})")
