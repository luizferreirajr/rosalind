"""
This program should receive a string and 4 indexes (a, b, d and d).
Then it will search the slice of this string from indices a through b and c through d (with space in between).
"""

sample = input('Enter a new string: ')

a = input('Enter the index a: ')
b = input('Enter the index b: ')
c = input('Enter the index c: ')
d = input('Enter the index d: ')

print(sample[a:b+1] + sample[c:d+1])


