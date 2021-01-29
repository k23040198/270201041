def binary_to_dec(binary):
  summ=0
  length=len(binary)
  ind = 0
  while ind<=len(binary)-1:
    for i in binary:
      if i=="0":
        ind += 1
        continue
      elif i=="1":
        a=2**(length-ind-1)
        summ+=a
        ind+=1
    return summ
print(binary_to_dec("10010"))

def dec_to_binary(deci):
  binary=""
  while True:
    a=deci//2
    remaining_part = str(deci - (a * 2))
    deci=a
    binary+=remaining_part
    if a==0:
      break
  return binary[::-1]
print(dec_to_binary(18))

  
  
