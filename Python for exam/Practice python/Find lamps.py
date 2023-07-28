n = int(input("Enter length of the road :"))
m = int(input('Enter lamps :'))
k = int(input('enter brightness range :'))
pos=[]
dfl=0
count = 0
road = [0] * (n+1)

for i in range(m):
    p = int(input('enter pos {} :'.format(i)))
    pos.append(p)
# print(pos)
for i in range(len(pos)):
    road[pos[i]] == 1
# print(road)
for i in range(n+1):
    if road[i] != 1:
        dfl +=1
        if road[i] != 1:
            count +=1
        elif dfl >= 2 * k and road[i] == 1:
            dfl = 0
        elif dfl >= k and road !== 1 and (dfl+k) > n:
            count += 1

