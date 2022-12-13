from random import randint


def bezout_recursive(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a % b)
    return (x, y - (a // b) * x, g)


def prime(number):
    z = number
    counter = 0
    for i in range(1, z + 1):
        if z % i == 0:
            counter += 1
    return True if counter == 2 else False


print("Enter j")
j = int(input())
print("Enter e")
e = int(input())
print("Enter n")
n = int(input())

while True:
    q = randint(0, 1000)
    p = randint(0, 1000)
    if q * p == n and prime(p) == True and prime(q) == True:
        break
f = (p - 1) * (q - 1)
d = f + bezout_recursive(e, f)[0]
c = j ** d % n
print(c)
