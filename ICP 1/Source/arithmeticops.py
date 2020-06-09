# Enter two numbers
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
# Addition
add = num1+num2
print("Addition of %d and %d is %d" % (num1, num2, add))
# Subtraction
sub = num1-num2
print("Subtraction of %d and %d is %d" % (num1, num2, sub))
# Multiplication
mul = num1*num2
print("Multiplication of %d and %d is %d" % (num1, num2, mul))
# Division only possible if the denominator is non zero
if num2 != 0:
    div = num1/num2
    print("Division of %d and %d is %d" % (num1, num2, div))
else:
    print("Cannot Divide a number by zero")
