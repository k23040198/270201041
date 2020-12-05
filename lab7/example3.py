company=dict()
x=1
b=[]
while x<=5:
  name=input("enter your name:")
  salary=int(input("enter your salary:"))
  company[name]=salary
  x+=1
biggest_salaries=sorted(company.values())[-3:]
for i,y in company.items():
  if y in biggest_salaries:
    print(i)