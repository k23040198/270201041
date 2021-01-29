def selection_sort(list_):
  length=len(list_)
  for i in range(length-1):
    min_value=i
    for b in range(i+1,length):
      if list_[b]<list_[min_value]:
        min_value=b

    list_[i],list_[min_value]=list_[min_value],list_[i]

list_=[-8,4,6,98,-36,-63,89,10]
selection_sort(list_)
print(list_)

