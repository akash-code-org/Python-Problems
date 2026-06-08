temp = int(input("Enter tempreture: "))
if temp < 0 and temp > -1:
    print("Tempreture is cold: ")
elif temp > 1 and temp < 30:
        print("Tempreture is normal: ")
elif temp > 30:
    print("Tempreture is hot: ")
else:
    print("Tempreture is cold: ")