f_num=int(input("how many fibonnaci numbers do you want to write?: "))
a=0
b=1
d=[1]
for i in range(f_num-1):
  a=b+i
  d.append(a)
  if a==3:
    for _ in range(4,f_num-1):
      e=d[-1]+d[-2]
      d.append(e)
print(d)

  
  
    

  
  
  
  
  
  

