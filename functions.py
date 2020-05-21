print("Hello to functions lesson")

def calc1(a, b):
  c = a * a + b
  return c

x = calc1(4, 6)
print("The result")
print(x)
print("The result " + str(x) ) 

def calc2(a, b, c):
  summary = a + b + c
  return summary

Q = calc2(5, 3, 33)
print("Total " + str(Q) )