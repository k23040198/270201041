def merge(list_):
  if len(list_)>1:

    mid=len(list_)//2
    list_left=list_[:mid]
    list_right=list_[mid:]
   
    merge(list_left)
    merge(list_right)

    mergeSort(list_,list_left,list_right)


def mergeSort(list_,list_left,list_right):
  i,j,k=0,0,0

  while i<len(list_left) and j < len(list_right):
    if list_left[i]<=list_right[j]:
      list_[k]=list_left[i]
      i+=1
    else:
      list_[k]=list_right[j]
      j+=1
    k+=1
  
  while i < len(list_left):
    list_[k]=list_left[i]
    i+=1
    k+=1

  while j < len(list_right):
    list_[k]=list_right[j]
    j+=1
    k+=1


def selection_sort(arr,index=0):
  
  if index==len(arr):
    return arr
  
  minimum_value=arr[index]
  minimum_index= index

  for i in range(index,len(arr)):
    
    if arr[i]<minimum_value:
      minimum_value= arr[i]
      minimum_index=i

  if minimum_index!= index:
    arr[minimum_index],arr[index]=arr[index],arr[minimum_index]
  
  return selection_sort(arr,index+1)

list_=[-8,4,6,98,-36,-63,89,10]
selection_sort(list_)
print(list_)  

def pairStar(word):
    if len(word)==1:
        return word
    else:
      new=""
      if word[0]==word[1]:
        new=word[0]+"*"+pairStar(word[1:])
      else:
        new+=word[0]+pairStar(word[1:])
      return new

class Person:
  def __init__(self,id):
    self.id=id
    self.name=""
    self.surname=""

  def __str__(self):
    info="Person id: "+ str(self.id)
    if self.name: info+= "\nName:"+ str(self.getName())
    if self.surname: info+= "\nSurname:"+ str(self.getSurname())
    info+= "\nMother:"+ self.mother.getFullname()
    info+= "\nFather:"+ self.father.getFullname()
    return info

  def setName(self,name):
    self.name=name
    
  def setSurname(self,surname):
    self.surname=surname
    
  def getName(self):
    return self.name

  def getSurname(self):
    return self.surname

  def getFullname(self):
    return self.name + " " + self.surname

  def setMother(self,mother):
    self.mother=mother

  def setFather(self,father):
    self.father=father


p1=Person(1234)
p2=Person(5618)
p1.setSurname("Çevik")
p1.setName("Ebru")
p2.setName("Cihan")
p2.setSurname("Çevik")
p3=Person(9897)
p3.setName("Sude Nur")
p3.setSurname("Çevik")
p3.setMother(p1)
p3.setFather(p2)
print(p3)
p3.setName("ali")
print(p3)