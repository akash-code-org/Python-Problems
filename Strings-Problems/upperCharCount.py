s = input('Enter the string: ')
count = 0
for ch in s:
    if ch == ch.upper():
        count+=1

print(count)