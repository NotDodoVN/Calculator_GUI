# num1 = float(input("Please input 1 number: "))
# num2 = float(input("Please input 2 number: "))
#
# def add(first_num, second_num):
#     return first_num+second_num
#
# def minus(first_num, second_num):
#     return first_num- second_num
#
# def divide(first_num, second_num):
#     try:
#         first_num/second_num
#     except ZeroDivisionError:
#         return "Error"
#     except:
#         return "0"
#
# def multiply(first_num, second_num):
#     return first_num * second_num
#
# operation = input("What do you want to do? ")
#
# if operation == "add":
#     print(add(num1,num2))
# elif operation == "multiply":
#     print(multiply(num1,num2))
# elif operation == "divide":
#     print(divide(num1,num2))
# elif operation == "minus":
#     print(minus(num1,num2))



# num1 = int(input("Please input your number: "))
# binary = ""
#
# while num1 != 0:
#     if num1 % 2 == 1:
#         binary += "1"
#     else:
#         binary += "0"
#     num1 = num1 // 2
#
# print(binary[::-1])

# def recurssive(num1):
#     global binary
#     if num1 == 0:
#         print(binary[::-1])
#         return
#     if num1 % 2 == 1:
#         binary += "1"
#     elif num1%2 == 0:
#         binary += "0"
#     recurssive(num1//2)
#
# recurssive(num1)

from enum import Enum
class Hex_num(Enum):
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15

hex = "3Z"
result = 0
counter = len(hex) - 1

for x in hex:
    try:
        if x.isnumeric() == True:
            result += int(x) * (16**counter)
        else:
            result += Hex_num[x].value* (16**counter)
        counter -= 1
    except:
        hex = str(input("Please input the hex again: "))
print(result)

# x = ["Hello", 1, 2, 3]
# y = x
# print(y)
# y[2] = "LOL"
# x[1] = "BOOOM"
# print(x)