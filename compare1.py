a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if a == b and b == c:
    print("Numbers are equals:")
elif a < b and a < c:
    print("Smallest is: ",a)
elif b < c:
    print("Smallest is: ",b)
else:
    print("Smallest is: ",c)