#!/usr/local/bin/python3

input="target area: x=253..280, y=-73..-46"
test="target area: x=20..30, y=-10..-5"

x1=253
x2=280
y1=-73
y2=-46

# x1=20
# x2=30
# y1=-10
# y2=-5

max_height = 0
possible_shots = 0

def inverse_triangle(num):
    total = 0
    i = 0
    while total < num:
        i += 1
        total += i

    return i

def hit(x, y):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

def simulate(i, j):
    global max_height
    global possible_shots
    x = 0
    y = 0
    xvel = i
    yvel = j
    height = 0
    while y >= y1:
        x += xvel
        y += yvel
        height = max(y, height)
        xvel = max(0, xvel-1)
        yvel -= 1
        if hit(x,y):
            break;

    if hit(x,y):
        possible_shots += 1

    if hit(x,y) and height >= max_height:
        max_height = height

for i in range(0, x2+1):
    for j in range(y1, (x2+y2)):
        simulate(i, j)

print("Out of", possible_shots, "possible shots,", max_height, "was the highest.")

