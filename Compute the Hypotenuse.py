import math
height = int(input("Enter the height of the triangle in meters: "))
length = int(input("Enter the length of the triangle in meters: "))
print ("The length of the hypotenuse is ", round((math.sqrt(height ** 2 + length ** 2)), 2), " meters")