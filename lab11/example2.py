import random

def roll_die():
  return random.randint(1,6)

def roll_die_until_lucky_value(lucky_value):
  for a in range(6):
    num = roll_die()
    if num != lucky_value:
      print(num)
    else:
      break
roll_die_until_lucky_value(5)