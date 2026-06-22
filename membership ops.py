print("Enter your grades for each subject:")
Math=float(input("Math:"))
Reading=float(input("Reading:"))
Science=float(input("Science:"))
Social_Studies=float(input("Social Studies:"))
Writing=float(input("Writing:"))
final_grade_sum=(Math+Reading+Science+Social_Studies+Writing)
final_grade=final_grade_sum/5
validrange=range(0,101)
if final_grade not in validrange:
    print("Check your grades again! They are invalid.")
elif final_grade in range(91,101):
    print("Your final grade is A1.")
elif final_grade in range(81,91):
    print("Your final grade is A2.")
elif final_grade in range(71,81):
    print("Your final grade is B1.")
elif final_grade in range(61,71):
    print("Your final grade is B2.")
elif final_grade in range(51,61):
    print("Your final grade is C1.")
elif final_grade in range(41,51):
    print("Your final grade is C2.")
elif final_grade in range(41,31):
    print("Your final grade is D1.")
elif final_grade in range(31,21):
    print("Your final grade is D2.")
else:
    print("Your final grade is F.")
