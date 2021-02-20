def factorial(n):


number = -1
while number < 0:
  try:
    number = int(input("Give me a positive number: "))
  except:
    print("That wasn't a number.")
print(number,"factorial is",factorial(number))
