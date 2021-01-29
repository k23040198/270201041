list1=list()
numbers=int(input("How many numbers do you give?"))
for i in range(numbers):
    num=int(input("Please enter the number:"))
    if num in list1:
        continue
    else:
        list1.append(num)
list1.reverse()
print(list1)
