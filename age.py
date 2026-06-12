age = int(input("Enter your age: "))
if age <= 10:
    print("User is child: ")
elif age >= 11 and age < 18:
    print("User is teenager: ")
elif age >= 18:
    print("User is adult: ")