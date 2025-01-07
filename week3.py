#Minimum of two numbers
a=int(input())
b=int(input())
if(a>b):
    print(b)
else:
    print(a)

#Sign function
x=int(input())
if(x>0):
    print(1)
elif(x<0):
    print(-1)
else:
    print(0)

#Minimum of three numbers
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

#Equal numbers
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

#Rook move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

#Chess board - same color
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

#King move
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs(a-c)<=1 and abs(b-d)<=1:
    print("YES")
else:
    print("NO")

#Knight move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1-x2)
dy = abs(y1-y2)
if dx == 1 and dy == 2 or dx == 2 and dy ==1:
    print("YES")
else:
    print("NO")

#Chocolate bar
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')

#Leap year
a=int(input())
if(a%4==0) and (a%100!=0) or (a%400==0):
    print("LEAP")
else:
    print("COMMON")

