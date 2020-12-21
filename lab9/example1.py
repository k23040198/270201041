def harmonic(x):
  if x == 1:
    return 1

  else:
    return harmonic(x-1) + 1/x

a=harmonic(5)
print(a)