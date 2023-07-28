
## create a program to find the

##print welcome
"""
M represent  length of road
N represent for number of lamps
K represent illuminate capacity

first represent space of front line that has no light
last represent space of back line that has not light
between represent space between lamp to lamp that has no light

min_lamp represent the needed lamps
"""

#print welcome message
print("======== Welcome My Friends ========")
# let user input the M N K and position of each lamp
M = int(input("Enter length of road: "))

# let user input the number streetlight
i = 0
while i < 1:
    N = int(input("Enter the number of lamps on the road: "))
    if 1 <= N <= M:
        i = i + 1
    else:
        print("Wrong Input!! number of lamps should not less than 1 and greater than ", M)
        print("Input Again! 💥")

# let user input the capacity of illuminate
i = 0
while i < 1:
    K = int(input("Enter the illuminate capacity of lamps: "))
    if K > 0:
        i = i + 1
    else:
        print("Wrong Input!! illuminate must be greater than 0")
        print("Input Again! 💥")


##creat a list to store position of each lamp
position = []
# let user input the
for i in range(N):
    p = int(input("Enter position of streetlight:"))
    position.append(p)
#  create variable to store first last and between street light
min_street_light = 0
first = 0
last = 0
between = 0

first = position[0] - K
last = position[-1] + K

# find first
if first > 0:
    if first <= (2*K - 1):
        min_street_light = min_street_light + 1
    elif (first % (2*K)) == 0 and (first >= (2*K)):
        min_street_light = min_street_light + (first // (2 * K))
    else:
        min_street_light = min_street_light + (first // 2 * K) + 1

#find last
if M - last > 0:

    if M - last <= ((2 * K) - 1):
        min_street_light =  min_street_light + 1
    elif (M - last) % (2 * K) == 0 and (M - last) >= 2*K:
        min_street_light = min_street_light + ((M - last) // (2 * K))
    else:
        min_street_light = min_street_light + ((M - last) // (2*K)) + 1

#find lamps between
for i in range(len(position) - 1):
    between = (position[i + 1] - K) - (position[i] + K)
    if between > 0:
        if between <= 2*K - 1:
            min_street_light = min_street_light + 1
        elif between % (2 * K) == 0 and between >= 2*K:
            min_street_light = min_street_light + (between // (2 * K))
        else:
            min_street_light = min_street_light + (between // 2*K) + 1
    between = 0
print("The minimum lamp is: ", min_street_light)









