a = [1,2,3,4,7]
b = [3,2,1,5,7]
for i in b:
    if i not in a:
        a.append(i)
print(a)