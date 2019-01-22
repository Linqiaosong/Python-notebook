# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:24:04 2019
structure statement

@author: linqi
"""
# if statement-------------------------------
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
#---------------------------------------------

# for statement-------------------------------
"""
Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.    

"""
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
"""
output:
cat 3
window 6
defenestrate 12
"""
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
#words=['defenestrate', 'cat', 'window', 'defenestrate']
        
#----------------------------------------------
        
# range() function-----------------------------
for i in range(5):
    print(i) #output:0,1,2,3,4
range(5, 10) #output:5,6,7,8,9
range(0, 10, 3) #output:0,3,6,9
range(-10, -100, -30) #output:-10,-40,-70
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
"""
output:
0 Mary
1 had
2 a
3 little
4 lamb
"""
print(range(10)) #error! output:range(10)
#if you want to print a range object, you should use list()
list(range(5)) #output:[0, 1, 2, 3, 4]

#-----------------------------------------------

# break and continue Statements, and else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:# loop fell through without finding a factor
        print(n, 'is a prime number')
"""
output:
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
"""
#The continue statement, also borrowed from C, continues with the next iteration of the loop

#-----------------------------------------------

# pass Statements--------------------------------
while True:
    pass 
#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
#-----------------------------------------------
    
# Defining Functions-----------------------------
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print() # print or return
#------------------------------------------------