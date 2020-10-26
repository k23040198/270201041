#gpa=float(input("please enter your gpa:"))
#num_of_lec=int(input("please enter your number of lectures:"))
#if gpa<2.0 and num_of_lec<47:
  #print("it is not enough number of lectures and gpa.")
#elif gpa<2.0 or num_of_lec>=47:
  ###print("it is not enough gpa.")
#elif gpa>=2.0 and num_of_lec<47:
  #print("not enough number of lectures")
#else:
  #print("you are gratuated")

x=int(input("please enter your age:"))

number_ticket_price=3
the_free_price=0
the_discount_price=1.5

if x<6 or x>60:
  print("the price is:",the_free_price)
elif 6<x<18 :
  print("the price is:", the_discount_price)
else:
  print("the price is:",number_ticket_price)