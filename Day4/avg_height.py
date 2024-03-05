student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total=0
for i in student_heights:
  total+=i
print(f"total height = {total}")
num = 0
for i in student_heights:
  num+=1
print(f"number of students = {num}")

avg =round(total/num)
print(f"average height = {avg}")
  