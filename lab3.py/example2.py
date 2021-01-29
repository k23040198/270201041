num1=input("Please enter a number1:")
num2=input("Please enter a number2:")
num3=input("Please enter a number3:")

if num1<num2 and  num1<num3:
	print("minimum value is:",num1)
elif num2<num3 and  num2<num1:
	print("minimum value is:",num2)
else:
	print("minimum value is:",num3)

