#enter the values 

total1 = float(input("Enter the total cost: "))
total2 = float(input("Enter the amount of money you paid: "))
c = float(total2 - total1)
c1 = c*100
c2 = round(c1/5.0)*5.0

n = c2//200
r1 = c2%200

n2 = (r1//100) 
r2 = r1%100

n3 = (r2//25)
r3 = r2%25

n4 = (r3//10)
r4 = r3%10

n5 = (r4//5)
r5 = (r4%5)
#print values

print(str(n) +" toonies," + str(n2) + " loonies," + str(n3) + "quarters," + str(n4) + " dimes and," + str(n5) + " nickels")