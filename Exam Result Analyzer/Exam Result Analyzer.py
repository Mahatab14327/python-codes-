print("Exam Result Analyzer")

subjects = int(input("Enter the number of subjects:"))
total = 0
for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}:"))
    total = total + marks

percentage = (total / subjects)
if percentage >= 100:
    grade = "A+"
if percentage >= 90:
    grade = "A+"
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "A-"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# pass / fail
if percentage >= 40:
    status = "Pass"
else:
    status = "Fail"
    
    print("\n Result-")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Status:", status)