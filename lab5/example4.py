defined_password="123456"
index=0
while True:
  password=input("please enter the password: ")
  if defined_password==password:
    print("welcome!!")
    break
  elif password=="help":
    print(defined_password[0+index])
    index+=1
  else:
    print("the password that you are writing is wrong!")