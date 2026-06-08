temp = int(input("Enter tempreture: "))
if temp > 1 and temp < 30:
    print("Tempreture is normal: ")
elif temp > 30 and temp < 60:
    print("Tempreture is hot: ")
else:
    print("Tempreture is cold: ")