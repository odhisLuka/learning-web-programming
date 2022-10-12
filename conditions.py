n = int(input("Number: "))
# you need to define the variable n as an integer, otherwise when you run n, you will get a typeError
# because the computer can't distinguish whether n is a str or and int

if n > 0:
  print("n is positive")
elif n < 0:
  print("n is negative")
else:
  print("n is zero")
