a = int(input("Enter first number: "))
b = int(input("Enter second number; "))
op = input("Enter your operation *,-,+,/")
if op == "*":
    print(a*b)
elif op == "-":
    print(a-b)
elif op == "+":
    print(a+b)
else:
    print(a/b)