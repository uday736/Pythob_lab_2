import calculator

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiplication(a, b))
print("Division:", calculator.divide(a, b))
print("Percentage:", calculator.percentage(a, b))