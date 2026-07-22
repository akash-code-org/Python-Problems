n = int(input('Enter the number: '))
L = [1,2,2,3,2,1,2,4,5]
count = 0
for i in L:
    if i == n:
        count+=1

print(count)

