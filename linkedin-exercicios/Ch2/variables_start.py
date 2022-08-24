# 
# Example file for variables
#

# Declare a variable and initialize it
from distutils import bcppcompiler


f=0
# print(f)



# re-declaring the variable works
# f='abc'
# print(f)


# ERROR: variables of different types cannot be combined
# print( "this is a string " + str(123))


# Global vs. local variables in functions

def MyFunction():
    f="def"      # variavel local
    print(f)

def MyFunction2():
    global f
    f="def"    # variavel f se tornou global
    print(f)


MyFunction2()
print(f)

# del f
# print (f)


