n = int(input("Enter a number: "))
sum = 0
lastDigit = 0
while n!=0:
    lastDigit = n%10
    sum+=lastDigit
    n//=10

print("The sum of digit is: ",sum)