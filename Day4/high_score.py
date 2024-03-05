student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
score = 0
for i in student_scores:
  if i >score:
    score = i
print(f"The highest score in the class is: {score}")