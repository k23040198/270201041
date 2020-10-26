gpa=float(input("please enter your gpa:"))
num_of_lec=int(input("please enter your number of lectures:"))

if gpa<2.0 and num_of_lec<47:
  print("it is not enough number of lectures and gpa.")
elif gpa<2.0 or num_of_lec>=47:
  print("it is not enough gpa.")
elif gpa>=2.0 and num_of_lec<47:
  print("not enough number of lectures")
else:
  print("you are gratuated")