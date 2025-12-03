with open('./data.txt', "r") as f: content = f.readlines()

start = 50
total = 0
for line in content:
    d = line.strip()[:1]
    r = int(line.strip()[1:])
    if d == 'L':
        start = (start - r) % 100
    elif d == 'R':
        start = (start + r) % 100
    print(start)
    if start == 0:
        total += 1
print(total)