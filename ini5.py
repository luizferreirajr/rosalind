"""
    This program receive a file with n lines and return a new file containing all the even-numbered lines
     from the original file. Assume 1-based numbering of lines.
"""

f = open('rosalind_ini5.txt', 'r')
s = open('newfile.txt', 'w')
index = 0

for i in f:
    if index % 2 == 1:
        s.write(str(i))
    index += 1

f.close()
s.close()
