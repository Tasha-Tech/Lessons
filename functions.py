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

# Homework !!!
# Define function named calc3
# This function will receive one argument
# it will calculate qubic value of this argument
# and also this function will print argument and it's qubic value
# Call this function two times.
# Result should look like:
# Value 5 in power of 3 is 125
# Value 3 in power of 3 is 27
