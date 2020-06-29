"""
This program should receive 2 numbers, then it will sum all the odd numbers between them
"""

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
sum = 0

for i in range (num1, num2+1):
    if i % 2 == 1:
        sum += i
    else:
        sum = sum

print('The sum of the odd numbers is: ' + str(sum))