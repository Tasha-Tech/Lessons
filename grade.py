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