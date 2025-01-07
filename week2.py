#Last digit of integer
a=int(input())
print(a%10)

#Tens digit
n = int(input())
print(n // 10 % 10)

#Sum of digits
a=int(input())
print((a//100)+(a//10%10)+(a%10))

#Fractional part
a=float(input())
print(a-int(a))

#First digit after decimal point
a=float(input())
print(int(a*10)%10)

#Car route
from math import ceil
n=int(input())
m=int(input())
print(ceil(m/n))

#Digital clock
n=int(input())
h=n//60
m=n%60
print(h, m)

#Total cost
a=int(input())
b=int(input())
n=int(input())
cost=n*(100*a+b)
print(cost//100, cost%100)

#Clock face - 1
h=int(input())
m=int(input())
s=int(input())
print(h*30+m*30/60+s*30/3600)

#Clock face - 2
alpha=float(input())
print(alpha%30*12)
