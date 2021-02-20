def factorial(n):
  f = 1
  for x in range(2,n+1):
    f = f * x
  return f

number = -1
while number < 0:
  try:
    number = int(input("Give me a positive number: "))
  except:
    print("That wasn't a number.")
print(number,"factorial is",factorial(number))
