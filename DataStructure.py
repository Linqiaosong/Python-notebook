# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:24:16 2019
data structure

@author: linqi
"""

# Strings-----------------------------------------------------
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

"""
output:
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
3 * 'un' + 'ium' #output:'unununium'
'Py' 'thon' #output:'python'
word = 'Python'
word[0] #output: 'P'
word[5] #output: 'n'
#Indices may also be negative numbers, to start counting from the right:
word[-2] #output: 'o'
word[2:5] #output: tho'
word[:2]   # character from the beginning to position 2 (excluded)
# output: 'Py'
word[4:]   # characters from position 4 (included) to the end
# output : 'on'
len(word) #output:6
# The built-in function len() returns the length of a string

#---------------------------------------------------------------

# list----------------------------------------------------------
squares = [1, 4, 9, 16, 25]
squares[0] #output: 1
squares[-1] #output: 25
squares[-3:] #output: [9, 16, 25]
squares + [36, 49, 64, 81, 100] 
#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content
squares[3] = 64 #squares=[1, 4, 9, 64, 25]
#You can also add new items at the end of the list, by using the append() method (we will see more about methods later
squares.append(216) #squares=[1, 4, 9, 64, 25, 216]
#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
squares[-3:]=[] #squares=[1, 4, 9]

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') #Return the number of times x appears in the list.
fruits.index('banana') 
fruits.reverse() #Reverse the elements of the list in place.
fruits.append('grape') #Add an item to the end of the list.
fruits.sort() #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
"""
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
"""
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""
equal to:
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
"""

#Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],]
#transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]
#---------------------------------------------------------------

# del statement-------------------------------------------------
#The del statement can also be used to remove slices from a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # a=[1, 66.25, 333, 333, 1234.5]
del a[2:4] # a=[1, 66.25, 1234.5]
del a[:] # a=[]
del a # delete entire variables a
#---------------------------------------------------------------

# tuples and sets-----------------------------------------------

#turples: A tuple consists of a number of values separated by commas
t = 12345, 54321, 'hello!'
t[0] #output: 12345
t #output: (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u #output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable!!!

#sets: A set is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
"""
output:
0 tic
1 tac
2 toe
"""

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
output:
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
"""

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
"""
output:
apple
banana
orange
pear
"""

#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

#----------------------------------------------------------------

# dictionary-----------------------------------------------------
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel #output: {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack'] #output: 4098

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# output: {'sape': 4139, 'guido': 4127, 'jack': 4098}
{x: x**2 for x in (2, 4, 6)}
#output: {2: 4, 4: 16, 6: 36}

#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
"""
output:
gallahad the pure
robin the brave
"""
#------------------------------------------------------------------