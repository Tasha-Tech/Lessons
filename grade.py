print("Welcome to a condition lesson!")

def grade1(x):
  if x > 90:
    return "A"

  if x > 80:
    return "B"

  if x > 70:
    return "C"

  if x > 60: 
    return "D"

  return "F"

y = grade1(95)
print("Your grade is " + y)

y = grade1(36)
print("Your grade is " + y)

y = grade1(87)
print("Your grade is " + y)

def grade2(q):
  if q <= 60:
    return "F"
  
  if q <= 70:
    return "D"

  if q <= 80:
    return "C"

  if q <= 90:
    return "B"

  return "A"

Z = grade2(51)
print("Your grade is " + Z)

Z = grade2(88)
print("Your grade is " + Z)

# Z = grade2(92)
print("Your grade is " + grade2(92))

def grade3(name, grade):
  if grade > 90:
    print(name  + " " + str(grade)  + " A")
    return "A"

  if grade > 80:
    print(name  + " " + str(grade)  + " B")
    return "B"

  if grade > 70:
    print(name  + " " + str(grade)  + " C")
    return "C"

  if grade > 60: 
    print(name  + " " + str(grade)  + " D")
    return "D"

  print(name  + " " + str(grade)  + " F")
  return "F"

y = grade3('Honey pie', 82)
print("Your grade is " + y)

y = grade3('youYouy', 36)
print("Your grade is " + y)

s = 'XYZ'
y = grade3(s, 87)
print("Your grade is " + y)

print("==================================")

def grade4(name, grade):
  score = ""

  if grade > 90:
    score = "A"
  elif grade > 80:
    score = "B"
  elif grade > 70:
    score = "C"
  elif grade > 60:
    score = "D"
  else:
    score = "F"

  print("Student " + name + " " + score)
  return score
  
y = grade4('Honey pie', 82)

y = grade4('YOUyuy', 16)

y = grade4('kuku', 76)

def grade5(name, grade):
  score = ""

  if grade > 90:
    score = "A"
  elif grade > 80:
    score = "B"
  elif grade > 70:
    score = "C"
  elif grade > 60:
    score = "D"
  else:
    score = "F"

  print("Student " + name + " " + score + " (" + str(grade) + ")")
  return score
  
y = grade5('Honey pie', 82)

y = grade5('YOUyuy', 16)

y = grade5('kuku', 76)






  

