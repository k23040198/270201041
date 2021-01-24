def selection_sort(list_):
  length=len(list_)
  round_=0
  
  for i in range(length-1):
    min_value=i
    for b in range(i+1,length):
      round_+=1
      if list_[b]<list_[min_value]:
        min_value=b

    list_[i],list_[min_value]=list_[min_value],list_[i]

  return round_

list_=[-8,4,6,98,-36,-63,89,10]

print(selection_sort(list_))

print(list_)



