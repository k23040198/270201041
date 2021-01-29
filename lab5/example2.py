number=int(input("How many numbers?"))
list_num,list_num2=list(),list()
for i in range(number):
    number2=int(input("Enter an integer:"))
    list_num.append(number2)
for a in list_num:
        if a %2==0:
            list_num2.append(a)
solution=(len(list_num2)*100)/(len(list_num))
print("%",solution)





