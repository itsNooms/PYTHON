##String

#Slices
a=str(input())
print(a[2])
print(a[-2])
print(a[:5])
print(a[0:-2])
print(a[0::2])
print(a[1::2])
print(a[::-1])
print(a[::-2])
print(len(a))

#The number of words
s=input()
print(len(s.split()))

#The two halves
s=input()
k=len(s)
print(s[(k+1)//2:]+s[:(k+1)//2])

#To swap the two words
s=input()
k=s.split()
print(k[1]+' '+k[0])

#The first and last occurrence
s=input()
k=s.find('f')
m=s.rfind('f')
if k==-1:
    print()
elif k!=m:
    print(k,m)
elif k==m:
    print(k)

#The second occurrence
s=input()
c=s.count('f')
if c==0:
    print(-2)
if c==1:
    print(-1)
if c>1:
    print(s.find('f',s.find('f')+1))

#Remove the fragment
s=input()
s=s[:s.find('h')]+s[s.rfind('h')+1:]
print(s)

#Reverse the fragment
s=input()
a=s[:s.find('h')]
b=s[s.find('h'):s.rfind('h')+1]
c=s[s.rfind('h')+1:]
s=a+b[::-1]+c
print(s)

#Replace the substring
print(input().replace('1','one'))

#Delete a character
print(input().replace('@',''))

#Replace within the fragment
s = input()
n1 = s.find("h")
n2 = s.rfind("h")
r = s[n1+1:n2].replace("h", "H")
t = s[:n1+1]
u = s[n2:]
print(t+r+u)

#Delete every third character
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
