student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = 'Outstanding'
    elif score >= 81:
        student_grades[key] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[key] = 'Acceptable'
    elif score <= 70:
        student_grades[key] = 'Fail'

# 🚨 print grade analysis👇
print(student_grades)



