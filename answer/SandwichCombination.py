

# ###create 4 list of breads, meats, vegetable and sauces
# breads = ["Khmer bread", "Chinese Bread", "Europe Bread", "Koread Bread"]
# meats = ["Ham", "Sausage", "Chicken", "Beef", "Frog"]
# vegetables = ["chilli", "tomato", "onion", "strawberry", "potato"]
# sauce = ["hot chilli", "ketchup", "mayo", "Soybean", "Terk trey koh kong"]
#
# # let loop throug all the combination
# resuts = [(i + " " + j + " " + k + " " + l) for i in breads for j in meats for k in vegetables for l in sauce ]
# print(resuts)


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




######### List
#
# n = list(range(1, 101))
# sumX = 0
# for i in n:
#     sumX = sumX+ i
#
# print(sumX)




