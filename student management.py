print("===== Student Grade Calculator =====")

name = input("Enter Student Name: ")

maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))

total = maths + science + english
percentage = total / 3

print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")

if percentage >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
