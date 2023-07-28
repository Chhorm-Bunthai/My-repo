# list1 = [1,2,3,4,5,6,7,8,9,10]
# sum1 = sum(list1)
# print(sum1)

# Factorial

n = int(input("Please enter a number:"))
fact = 1
for i in range(1,n+1):
    fact *= i
print(str(n)+"! =",fact)