import random
n = random.randint(0,2)
if n == 0:
    computer = "left"
elif n == 1:
    computer = "center"
else:
    computer = "right"
shoot = input("Please choose direction to shoot (left,center,right)")
if computer == shoot:
    print("No goal!")
else:
    print("Goal!")

print("computer side:",computer)
print("Game over")