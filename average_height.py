# this will calculate the average height
# without using built in len or sum functions
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


len = 0
sum = 0

for st_height in student_heights:
    len +=1
    sum += st_height

print(len)
print(sum)
print(round(sum/len))
