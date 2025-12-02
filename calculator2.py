 Python Code: Student Grade Calculator

# Student Grade Calculator

# Input marks of 5 subjects
print("Enter marks of five subjects out of 100:")

m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Output result
print("\n----- Result -----")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")


