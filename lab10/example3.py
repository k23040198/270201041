a=input("string:")
def control(string):
  if len(string)==0:
    count=0
    return count

  else:
    if string[-1:].isalnum():
      count=0
      return count + control(string[:-1])
    else:
      count=1
      return count + control(string[:-1])

print(control(a))