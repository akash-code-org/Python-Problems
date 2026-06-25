n = int(input("Enter the number: "))
a = 1
b = 1
sum = 1
for i in range(1,n+1):
    sum = a+b
    a = b
    b = sum

print(sum)