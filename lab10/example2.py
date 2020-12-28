def multiple(x):
  if x==0:
    return 0

  return multiple(x-1)+3

print(multiple(6))