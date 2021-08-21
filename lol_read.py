import random

f = open("LOL_level1.txt", "r")
raw_data = f.readlines()

all_data = []
for i in range(len(raw_data)):
    t = raw_data[i].split()

    if i != 0:
        for j in range(1, len(t)):
            t[j] = float(t[j])

        t.insert(0, i)
    else:
        t.insert(0, "순번")
        
    all_data.append(t)

def p():
    r = random.randint(1, len(all_data)-1)
    print(all_data[0])
    print(all_data[r])
    return r

def show(first, last):
    print(all_data[0])
    for i in range(first, last):
        print(all_data[i])
