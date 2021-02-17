def greater(a=10, b=20, c=30): # default values

  if (a > b and a > c):
    print("a is greater than b and c")
  elif (a < c):
    print("c is greater than a and b")
  else:
    print("b is greater than a and c")


def difference(a, b):
  c = a - b
  return c
