print("""Welcome to Fly Trust foundation

Please provides your information for eligiblity""")
age = int(input("Enter the age: "))
gender = input("Enter the gender: ")
if age >= 50:
    pass
elif gender == 'female' or gender == 'Female':
    print("You are eligible for fly trust fund ")
else:
    print("Your not eligible for fly trust fund: ")