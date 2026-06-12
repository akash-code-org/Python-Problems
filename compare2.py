a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter forth number:"))
if a == b and b == c and c == d:
    print("Numbers are equals:")
elif a < b and a < c and a < d:
    print("Smallest is: ",a)
elif b < c and b < d:
    print("Smallest is: ",b)
elif c < d:
    print("Smallest is: ",c)
else:
    print("Smallest is: ",d)