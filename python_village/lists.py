"""
This program should receive a string and 4 indexes (a, b, d and d).
Then it will search the slice of this string from indices a through b and c through d (with space in between).
"""

sample = input('Enter a new string: ')

a = int(input('Enter the index a: '))
b = int(input('Enter the index b: '))
c = int(input('Enter the index c: '))
d = int(input('Enter the index d: '))

print(sample[a:b+1] + ' ' + sample[c:d+1])


