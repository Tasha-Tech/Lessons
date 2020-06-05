print("Choices")

def boobsSize(measurement):
  S = ""

  if measurement < 30:
    S = "A"
  elif measurement < 40:
    S = "B" 
  elif measurement < 50:
    S = "C"
  elif measurement < 60:
    S = "D"
  else:
    S = "DD"

  print("Size " + str(measurement) + " is " + S)
  return S

L = boobsSize(35)
