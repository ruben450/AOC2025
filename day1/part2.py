import math


with open('./data.txt', "r") as f: content = f.readlines()

start = 50
total = 0
for line in content:
    d = line.strip()[:1]
    r = int(line.strip()[1:])
    if d == 'L':
        temp = (start - r)
        if temp < 0 and start != 0:
            total += 1 + math.floor((abs(temp) / 100))
        start = (start - r) % 100
    elif d == 'R':
        if r > 100:
            total += math.floor((r / 100))
        start = (start + r) % 100
    if start == 0:
        total += 1
print(total)