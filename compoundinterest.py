#get amount of money first deposited 
p = int(input("Enter your savings: " ))
n = int(input("Enter the amount of time interest is applied: "))
r = (0.04) 

#interest you get yearly 
a1 = round((p * (1 + r/n)**(n*1)), 2)
a2 = round((p * (1 + r/n)**(n*2)), 2)
a3 = round((p * (1 + r/n)**(n*3)), 2)

#print statements
print("You have $" + str(a1) + " in your bank account after 1 year")
print("You have $" + str(a2) + " in your bank account after 2 year")
print("You have $" + str(a3) + " in your bank account after 3 year")