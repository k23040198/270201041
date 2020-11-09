year=int(input("enter a year:"))

if year%4==0 and (year%100!=0 or year%400==0):
  is_leap= True
else:
  is_leap= False

if is_leap:
  print("it is a leap year")
else:
  print("it is not a leap year.")