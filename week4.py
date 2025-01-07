#For loop with range

#Series - 1
A=int(input())
B=int(input())
for i in range (A,B+1):
    print(i)

#Series - 2
A=int(input())
B=int(input())
if A<B:
    for i in range (A,B+1):
        print(i)
else:
    for i in range (A,B-1,-1):
        print(i)

  #Sum of ten numbers
  n = 0
for i in range(10):
    n += int(input())
print(n)

#Sum of N numbers
n=int(input())
m=0
for i in range(n):
    m+=int(input())
print(m)

#Sum of cubes
n=int(input())
m=0
for i in range(1,n+1):
    m+=i*i*i
print(m)

#Factorial
n=int(input())
fact=1
for i in range(1, n+1):
    fact = fact * i
print(fact)

#The number of zeros
n=int(input())
c=0
for i in range(n):
    if int(input())==0:
        c+=1
print(c) 

#Adding factorials
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)

#Ladder
n=int(input())
s=""
for i in range(1,n+1):
    s+=str(i)
    print(s)

#Lost card
n=int(input())
s=n*(n+1)/2
for i in range(1,n):
    s-=int(input())
print(int(s))
