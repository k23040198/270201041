def tamsayböl(sayı):
  bölenler=[]
  for i in range(1,sayı+1):
    if sayı%i==0:
      bölenler.append(i)

  return bölenler

print(tamsayböl(120))

def ekok_(sayı1,sayı2):
  çarpım=sayı1*sayı2
  ekokSay=0
  for i in range(çarpım,1,-1):
    if çarpım%sayı1==0 and çarpım%sayı2==0 :
      ekokSay = çarpım
  return ekokSay

def ekok_recursive(sayı1,sayı2,çarpım=sayı1*sayı2):
  if çarpım==1:
    return 1 
  else:
    if çarpım%sayı1!=0 and çarpım%sayı2!=0:
      return ekok_recursive(sayı1,sayı2,çarpım-1)
    elif çarpım%sayı1==0 and çarpım%sayı2==0 :
      return çarpım


def ebob_(sayı1,sayı2):
  çarpım_2=0
  for i in range(1,min(sayı1,sayı2)+1):
    if sayı1%i==0 and sayı2%i==0:
      çarpım_2=i
  return çarpım_2

print(ekok_(4,6))
print(ebob_(12,24))

print(ekok_recursive(4,6,24))