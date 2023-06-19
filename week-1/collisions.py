import math

rectangle1 = [int(n) for n in input().split()]
rectangle2 = [int(n) for n in input().split()]

height = (rectangle1[2] + rectangle2[2]) / 2
width = (rectangle1[3] + rectangle2[3]) / 2

min_distance = math.sqrt(height**2 + width**2)
distance = distance = math.sqrt((rectangle2[0] - rectangle1[0])**2 + (rectangle2[1] - rectangle1[1])**2)

if distance < min_distance:
    print(1)
if distance >= min_distance:
    print(0)