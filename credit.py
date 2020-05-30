print("Wellcome to credit homework!")

'''
1. Create function credit1
This function should have two arguments:
name: str - student name
grade: int - grade received by student
function will return string value "PASS" or "FAIL"
If grade is grater than 75, function shell returm "PASS",
otherwise "FAIL" shell be returned.
Write couple tests for this function.

2. Create function credit2
This function should have three arguments:
name: str - student name
grade: int - grade received by student
threshould: int - threshould for "PASS"
function will return string value "PASS" or "FAIL"
If grade is grater than threshould, function shell returm "PASS",
otherwise "FAIL" shell be returned.
Write couple tests for this function.
 
This will serve as prerequisite for default arguments
'''
def credit1(name, grade):
  default = "FAIL"

  if grade > 75:
    default = "PASS"

  print("Student " + name + " " + default)
  return default

y = credit1('Honey pie', 82)
y = credit1('YOUyuy', 16)

def credit1A(name, grade):
  default = "FAIL"

  if grade > 75:
    default = "PASS"
  else:
    default = "FAIL"

  print("Student " + name + " " + default)
  return default

y = credit1A('Honey pie', 82)
y = credit1A('YOUyuy', 16)

def credit2(name, grade, threshould):
  score = "X"

  if grade > threshould:
    score = "PASS"
  else:
    score = "FAIL"
  
  print(name + " is evaluated as " + score + " (" + str(grade) + ")")
  return score

y = credit2('Honey pie', 82, 95)
y = credit2('YOUyuy', 16, 7)

def choice(money):
  product = "X"
  
  if money >= 7:
    product = "pie"
    return product
  
  if money >= 5:
    product = "apple"  
    return product

  if money >= 3:
    product = "orange"  
    return product

Q = choice(4)
print("i can buy " + Q)

def choice(money):
  product = "X"
  
  if money >= 7:
    product = "pie"
  elif money >= 5:
    product = "apple"  
  elif money >= 3:
    product = "orange"  
  else:
    product = "nothing"
  
  print("I can buy " + product)
  return product 
    
Q = choice(2)
Q + choice(10)

print("=========================")

def choiceA(money):
  product = ""
  budget = money

  if budget >= 7:
    product = "pie"
    budget = budget - 7

  if budget >= 5:
    if product != "":
      product = product + ", "

    product = product + "apple"  
    budget = budget - 5

  if budget >= 3:
    product = product + ", orange"
    budget = budget - 3
  
  if product == "":
    product = "nothing"


  print("I can buy " + product)
  return product 
    
Q = choiceA(2)
Q = choiceA(10)
Q = choiceA(6)