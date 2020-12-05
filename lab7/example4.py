a=set([2,3,4,5,5,20,15])
b=set([10,20,20,15,30,40])
c=list()
for i in a:
  for z in b:
    if i==z:
      c.append(i)
a.difference_update(b)
a.update(b)
print(a)
