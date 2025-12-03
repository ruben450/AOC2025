with open('./data.txt', "r") as f: content = f.readline()

ids = []

for line in content.split(','):
    seq = line.split('-')
    ids.append((int(seq[0]),int(seq[1])))
total = 0
for id in ids:
    a = id[0]
    b = id[1]
    for x in range(a,b+1):
        first = str(x)[:len(str(x))//2]
        second = str(x)[len(str(x))//2:]
        if first == second:
            total += x
print(total)