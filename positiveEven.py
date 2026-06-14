n = int(input("Enter the number: "))
if n > 0 and n%2==0:
    print("Number is positive and even: ")
elif n > 0 and n%1==0:
    print("Number is pos, but not even: ")
else:
    print("Number is not pos and even: ")