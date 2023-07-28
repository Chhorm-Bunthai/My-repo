seats = int(input("How many seats do you want? : "))

sum = 1
for i in range(1, seats + 1):
    if i % 2 != 0:
        for j in range(sum, sum + seats):
            print(j, end= " ")
        print()
        sum = sum + seats
    else:
        for j in range(sum + (seats - 1), sum - 1, -1):
            print(j, end=" ")
        print()
        sum = sum + seats