##While loop

#List of squares
i=1
n=int(input())
while (i**2<=n):
    print(i**2)
    i=i+1

#Least divisor
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

#The power of two
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)

#Morning jog
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)

#The length of the sequence
len = 0
while int(input()) != 0:
    len += 1
print(len)

#The sum of the sequence
count=0
i=int(input())
while i!=0:
    count+=i
    i=int(input())
print(count)

#The average of the sequence
count=0
sum=0
i=int(input())
while(i!=0):
    count+=1
    sum+=i
    i=int(input())
print(sum/count)

#The maximum of the sequence
list=[ ]
i=int(input())
while i!=0:
    list.append(i)
    i=int(input())
max=max(list)
print(max)

#The index of the maximum of a sequence
largest=0
largest_index=-1
index=1
while True:
    num=int(input())
    if num==0:
        break
    else:
        if num>largest:
            largest=num
            largest_index=index
        index+=1
print(largest_index)

#The number of even elements of the sequence
i=int(input())
n=0
while i!=0:
    if i%2==0:
        n+=1
    i=int(input())
print(n)

#The number of elements that are greater than the previous one
i=int(input())
prev=0
c=0
while(i!=0):
    prev=i
    i=int(input())
    if(i>prev):
        c=c+1
print(c)

#The second maximum
x=int(input())
lst=[]
while x!=0:
    lst.append(x)
    x=int(input())
lst=[int(x) for x in lst]
lst.sort()
print(lst[-2])

#The number of elements equal to the maximum
max=0
num_max=0
element=-1
while element!=0:
    element=int(input())
    if element>max:
        max,num_max=element,1
    elif element ==max:
        num_max+=1
print(num_max)

#Fibonacci numbers
a=0
b=0
c=1
n=int(input())
while(a<n):
    b,c=c,b+c
    a=a+1
print(b)

#The index of a Fibonacci number
n=int(input())
a=0
b=1
c=1
ind=1
while c<n:
    c=a+b
    a=b
    b=c
    ind+=1
if c!=n:
    print(-1)
else:
    print(ind)

#The maximum number of consecutive equal elements
x=int(input())
prev=x
count=1
mcount=count
while x!=0:
    x=int(input())
    if x==prev:
        count+=1
        prev=x
    else:
        if count>mcount:
            mcount=count
        count=1
        prev=x
print(mcount)
