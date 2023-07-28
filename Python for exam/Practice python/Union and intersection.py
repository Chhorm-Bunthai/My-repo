list_a = [1, 2, 3, 4]
list_b = [3, 2, 1, 5]
j=0
for i in list_a:
    if i in list_b:
        j= j.append(i)
    if list_a not in j:
        j += i
print(j)