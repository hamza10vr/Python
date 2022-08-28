# this will calculate the average height
# without using built in len or sum functions
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


len = 0
total_height = 0

for height  in student_heights:
    len +=1
    total_height += height

print(f"Average height is = {round(total_height/len)}")
