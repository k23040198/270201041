def reverse(my_list):
  if len(my_list)==0:
    return []

  else:
    return [my_list[-1]] + reverse(my_list[:-1])

x=[1,2,3]
y=reverse(x)
print(y)


