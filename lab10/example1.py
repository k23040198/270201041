def hailstone(x):
  if x==1:
    return [1]
  elif x%2==0:
    return [x]+ hailstone(x//2)
  return [x]+ hailstone(3*x+1)

print(hailstone(5))