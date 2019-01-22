# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:26:00 2019
Classes

@author: linqi
"""

# Scopes and Namespaces----------------------------------------------
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam # The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.
        spam = "nonlocal spam"

    def do_global():
        global spam # The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global.
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

"""
output:
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""
#----------------------------------------------------------------------

# Classes--------------------------------------------------------------
class Complex:
    def __init__(self, realpart, imagpart):  # construction function
        self.r = realpart
        self.i = imagpart
    def addition(self, __a, __b):
        self.r1 = __a.r
        self.i1 = __a.i
        self.r2 = __b.r
        self.i2 = __b.i
        return (self.r1+self.r2, self.i1+self.i2)
        
x = Complex(3.0, -4.5)
print((x.r, x.i), x.addition(x,x))
# output: (3.0, -4.5) (6.0, -9.0)

"""
Inheritance:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

"""
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

#-----------------------------------------------------------------------
