age=int(input("Please enter your age:"))

if age <6 or age>60:
	print("Ticket is free")
elif age >6 and age<18:
	print("Ticket price is 1.5TL")
else:
	print("Ticket price is 3 TL")