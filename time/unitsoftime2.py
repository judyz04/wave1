#get the time

sec = int(input("Enter the time in seconds: "))

n = sec//(3600 * 24)
r1 = sec%(3600 * 24)

n2 = r1//3600
r2 = r1%3600

n3 = r2//60
r2 = r2%60

#print everything
print(str(n) +" days," + str(n2) + " hours," + str(n3) + "minutes.")