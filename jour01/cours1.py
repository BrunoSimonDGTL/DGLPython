# -*- coding: utf-8 -*-
"""
Formation digitalab
creer une calculette

@author: Bruno
"""
def add (num1, num2) :
    return num1 + num2

def substract (num1, num2) :
    return num1 - num2

def multiply (num1, num2) :
    return num1 * num2

def divide (num1, num2) :
    return num1 / num2

print ("Choose an operator: ")

print(" 1 for addition\n 2 for substraction\n 3 for multiplication\n 4 for division")

select = int(input("Select opertator: "))

number1=int(input("enter first number: "))
number2=int(input("enter second number: "))

res=0
if select == 1 :
    print(number1, " + ", number2, " = ", add(number1, number2))
elif select == 2 :
    print(number1, " - ", number2, " = ", substract(number1, number2))
elif select == 3 :
    print(number1, " * ", number2, " = ", multiply(number1, number2))
elif select == 4 :
    print(number1, " / ", number2, " = ", divide (number1, number2))
else :
    print("invalid input")

