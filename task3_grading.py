marks = int(input("Enter your marks:"))

if marks>=90 and marks<=100:
    grade = "A"
elif marks>=75 and marks<90:
    grade = "B"
elif marks>=60 and marks<75:
    grade = "C"
elif marks>=50:
    grade = "D"
if marks<50:
    grade = "F"
else:
    print("Invalid")

    print("Grade: ", grade)
