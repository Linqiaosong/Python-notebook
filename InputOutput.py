# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:35:16 2019
Input and Output

@author: linqi
"""

# number-----------------------------------------------------
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5  # division always returns a floating point number
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
#-------------------------------------------------------------

# input-------------------------------------------------------
d=input("Please input the data:") # d is a string
#-------------------------------------------------------------

# output------------------------------------------------------
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# output: The value of pi is approximately 3.142.

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
"""
output:
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""
# str.format()-----------------------------------------------
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# output: We are the knights who say "Ni!"
print('{0} and {1}'.format('spam', 'eggs'))
#output: spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
#output: eggs and spam
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
#output: This spam is absolutely horrible.
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
#output: The story of Bill, Manfred, and Georg.
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
"""
output:
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
"""
#-----------------------------------------------------------

# Reading and Writing Files---------------------------------
f = open('workfile', 'w')
#The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

#It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
with open('workfile') as f: 
    read_data = f.read()

#If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times.
f.closed

#f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
f.readline()
# output: 'This is the first line of the file.\n'
f.readline()
# output: 'Second line of the file\n'
f.readline()
# output: ''

#For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
for line in f:
    print(line, end='')
"""
output:
This is the first line of the file.
Second line of the file
"""

#If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
list(f)
f.readlines()

#f.write(string) writes the contents of string to the file, returning the number of characters written.
f.write('This is a test\n') # output: 15
#Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s) #output: 18

#f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
f.tell()

#To change the file object’s position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument.
f.seek(5)      # Go to the 6th byte in the file
f.seek(-3, 2)  # Go to the 3rd byte before the end
#A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
