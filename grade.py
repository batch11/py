def calculate_grade(total):
    if total >= 90:
        return "A"
    elif total >= 80:
        return "B"
    elif total >= 70:
        return "C"
    elif total >= 50:
        return "D"
    else:
        return "E"

marks = []
for i in range(5):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

average_marks = sum(marks) / 5
grade = calculate_grade(average_marks)

print(f"\nAverage Marks: {average_marks:.2f}")
print(f"Grade: {grade}")
