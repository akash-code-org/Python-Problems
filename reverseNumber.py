n = int(input("Enter a number: "))
r = 0
while n>0:
    r = r*10
    r = r+(n%10)
    n//=10

print("The reveresd number is: ",r)