def Crook (N):
  if (N > 0):
     print(N)
     Crook(N // 2)
  print(N + 1)


Crook(101)