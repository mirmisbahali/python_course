'''
Get num1 value
Get num2 value
If (num1 > num2)
    print(num1 is greater than num2)
else 
    print(num2 is greater than num1)
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if (num1 > num2):
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')