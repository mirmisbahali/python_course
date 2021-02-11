'''
Get num1 value
Get num2 value
If (num1 > num2)
    print(num1 is greater than num2)
else 
    print(num2 is greater than num1)
'''

'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if (num1 > num2):
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1 > num2 and num1 > num3):
    print(f'{num1} is greater than {num2} and {num3}')
elif (num1 < num3):
    print(f'{num3} is greater')
else:
    print(f'{num2} is greater')

'''
num1 = 4
num2 = 5
num3 = 2

num1 > num2 and num1 > num3
    num1 is greater
num1 < num3
    num3 is greater

num2 is greater

'''
