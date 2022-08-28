#calculates the max score from the list without using max() built-in
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for n in student_scores:
    if n > max_score:
        max_score = n

print(f"The highest score in the class is: {max_score}")

