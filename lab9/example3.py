def count_even(my_list):
  count=0
  for i in my_list:
    if i%2==0:
      count+=1
  return count
    
x=[1,2,3,4,5,6]
y=count_even(x)
print(y)

