# Getting user input numbers
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

# Getting user input operation
operation = input("enter the operation (+, -, *, /): ")

#perform the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation =='*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation =='/':
    if num2 != 0:
      result = num1 / num2
      print(f"{num1} / {num2}= {result}")
    else:
        print("error: division by zero is not allowed.")
else:
    print("invalid operation entered. Please use +, -, *, or /.")


