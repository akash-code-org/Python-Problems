n = int(input('Enter the number: '))
total = 1
for i in range(1,n+1*2//2):
    total += (total*i)//i

print(total)