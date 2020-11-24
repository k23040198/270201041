liste=input("please enter the list (x,y,z):")
a=set([])
b=[]
liste=liste.split(",")
for i in liste:
  e=int(i)
  a.add(e)
for c in a:
  b.append(c)
  b.sort()
print(b)