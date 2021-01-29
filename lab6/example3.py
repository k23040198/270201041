student=int(input("How many students do you have?:"))
grades=list()
for i in range(student):
  grade=int(input("Enter the grade:"))
  if grade>90:
    grades.append(grade)