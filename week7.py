##Lists

#Even indices
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])

#Even elements
a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)

#Greater than previous
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

#Neighbors of the same sign
st = input().split()
for i in range(len(st)-1):
    if int(st[i]) * int(st[i+1]) > 0:
        print(st[i], st[i+1], end = " ")
        break

#Greater than neighbours
a = [int(i) for i in input().split()]
n = 0
for i in range(1,len(a)-1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        n += 1
print(n)

#The largest element
a = [int(i) for i in input().split()]
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max, a.index(max))

#The number of distinct elements
a = [int(i)for i in input().split()]
n = 1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        n += 1
print(n)

#Swap neighbours
a = [int(i) for i in input().split()]
n = 0
for i in range(int(len(a)/2)):
    a[n],a[n+1] = a[n+1],a[n]
    n += 2
for i in a:
    print(i, end = " ")

#Swap min and max
a = [int(i) for i in input().split()]
max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
l = a.index(max)
m = a.index(min)
a[l],a[m] = a[m], a[l]
for i in a:
    print(i, end =" ")

#The number of pairs of equal
a = [int(i) for i in input().split()]
n = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            n += 1
print(n)

#Unique elements
a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end = " ")

#Queens
a = []
for i in range(8):
    ls = [int(i) for i in input().split()]
    a.append(ls)
n = 0
for i in range(8):
    for j in range(i+1,8):
        if abs(a[i][1]-a[j][1]) == abs(a[i][0]-a[j][0]):
            n += 1
        elif abs(a[i][1]-a[j][1]) == 0 or abs(a[i][0]-a[j][0]) == 0:
            n += 1
        else:
            n += 0
if n == 0:
    print("NO")
else:
    print("YES")

#The bowling alley
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))
