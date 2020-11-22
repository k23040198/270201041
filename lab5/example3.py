if len(num1) > len(num2):
for i in reversed(num1):
for x in reversed(num2):
if x == i:

match+=1

else:

for i in reversed(num2):

for x in reversed(num1):

if x == i:

match+=1

print(match)

