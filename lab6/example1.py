liste=input("please enter the list (x,y,z):")
a=[]
b=[]
liste=liste.split(",")
for i in liste:
  e=int(i)
  a.append(e)
for c in a:
  if c not in b:
    b.append(c)
b.sort()
print(b)