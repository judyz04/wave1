#get values from user
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
#change length and width into acres
l2 = length/43560
w2 = width/43560
#find area
area = l2*w2
area2 = round(area, 2)
print("The area is "+ str(area2) + " in acres.")