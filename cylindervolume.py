import math

#find all values
radius = int(input("Enter the radius value: "))
height = int(input("Enter the height value: "))

#find the area of the circle 
area1 = math.pi * radius ** 2

#find volume of cylinder
volume = round(area1*height, 1)

#print statement
print("The volume of the cylinder is " + str(volume) + ".")