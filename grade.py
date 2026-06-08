marks = int(input("Enter the marks: "))
if marks < 50:
    print("Fail: ")
elif marks >= 50 and marks < 60:
    print("D grade")
elif marks >= 60 and marks < 70:
    print("C grade")
elif marks >= 70 and marks < 80:
    print("B grade: ")
elif marks >= 80 and marks < 90:
    print("A grade: ")
else:
    print("A+ grade: ")