
import time
print("Welcome to my first python calcumalator")
number = float(input("input your first number: " ))
operator = input("input your operator")
number2 = float(input("input your second number: "))
if operator == '+':
    print(number + number2)
if operator == '-':
    print(number - number2)
if operator == '*':
    print(number * number2)
if operator == '/':
    if number2 == 0 :
        print("looks like you cant do this try a different number for this")
    else:
        print(number / number2)
