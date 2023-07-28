n = int(input('enter meter:'))
m = int(input('enter lamps:'))
k = int(input('enter length of b illuminate:'))
pos = int(input('enter pos you want to start:'))
pos2 = int(input('enter second pos you want to start:'))
m = list(range(1,3))

for i in m:
    if i == pos:
        i +=2
    if i == pos2:
        i +=2
