##Functions and recursion

#The length of the segment
def distance(x1, y1, x2, y2):
    import math
    dx = (x2-x1)
    dy = (y2-y1)
    distance = math.sqrt((dx**2) + (dy**2))
    return distance

print(distance(float(input()), float(input()), float(input()), float(input())))

#Negative exponent
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))

#Uppercase
def capitalize(a):
    st = a.split(" ")
    nst = []
    for i in range(len(st)):
        b = st[i]
        c = b[0].upper() + b[1:len(st[i])]
        nst.append(c)
    return(" ".join(nst))

print(capitalize(input()))

#Exponentiation
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))

#Reverse the sequence
def reverse():
    a = int(input())
    if a != 0:
        reverse()
    print(a)

reverse()

#Fibonacci numbers
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(int(input())))
