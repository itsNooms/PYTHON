##TDictionaries

#Number of occurrences
words = input().split()
for i in range(len(words)):
    print(words[:i].count(words[i]), end=' ')

#Dictionary of synonyms
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])

#Elections in the USA
n = int(input())
d = {}
for i in range(n):
    key, val = input().split()
    if key in d:
        d[key] += int(val)
    else:
        d[key] = int(val)
for key, val in sorted(d.items()):
   print(key, val)

#The most frequent word
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))

#Access rights
permissions = {}
n = int(input())
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input())):
    perm, file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permissions[file]:
        print('OK')
    else:
        print('Access denied')

#Countries and cities
  n = int(input())
cities = {}
for _ in range(n):
    line = input().split()
    for city in line[1:]:
        cities[city] = line[0]

for _ in range(int(input())):
    print(cities[input()])

#Frequency analysis
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

#English-Latin dictionary
from collections import defaultdict

lateng = defaultdict(list)
for i in range(int(input())):
    eng_word, lat_trans = input().split(' - ')
    lat_translations = lat_trans.split(', ')
    for lat_word in lat_translations:
        lateng[lat_word].append(eng_word)
        
print(len(lateng))
for lat_word, eng_translations in sorted(lateng.items()):
    print(lat_word + ' - ' + ', '.join(eng_translations))
