"""
def function1():
    print("Hello Good morning")

#function1()

def function2(msg):
    print(msg)

function2("We are laerning Python Programming")
function2("Functional programming")
function2(3456)
function2([3, 5, 6, 8])
"""

# scope of variables

var2 = 20 # global variable : scope of this variable is wider and can access by all the function

"""
point1 : if we have one local variable and global variable with different name then their scope
          will also be different.
point2 : local variable of one function can not call in another function.
point3 : if we have one local variable and global variable with same name, then local variable value
         will get preference in the function.
         
point4 : We can modify global variable value with global keyword with in any function and assign other value to same variable.
"""

def function3_scope():

    var1 = 10  # local variable : the scope is limited to function only.
    print(var1+var2)

def function4_scope():
    var3 = 30
    #print(var3+var1) we can not call local variable any other function to this function.


def function5():
    var2 = 40
    print("var2 :", var2)

def function6():
    print("global variable :", var2)

def function7():
    global var2
    var2 = 60
    print("var2 :", var2)


#function3_scope()
#function5()
#function6()

#function7()
#function6()



varp = 100 # global variable

def outer_function():
    varx = 30  # non local variable
    vary = 50  # non local variable

    def inner_function1():
        varz = 60  # local variable
        print("varz:", varz)
        print("varx:", varx)
        print("vary:", vary)
        print("varp:", varp)

    def inner_function2():
        nonlocal varx
        global varp
        varx = 40
        varp = 50
        print("varx:", varx)
        print("vary:", vary)
        print("varp:", varp)

    inner_function1()
    print("__"*20)
    inner_function2()
    print("__" * 20)
    inner_function1()


def outer_function2():
    print("varp:", varp)


outer_function2()
print("__" * 20)
outer_function()
print("__" * 20)
outer_function2()




