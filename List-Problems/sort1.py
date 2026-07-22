L = [1,4,3,4]
flag = True
for i in range(len(L)-1):
    if L[i] > L[i+1]:
        print("Not sorted: ")
        flag = False
        break

if(flag):
    print('Sorted: ')