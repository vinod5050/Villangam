#

def calc(a,b):# like inbuild function, not able to change
    print(a/b)

def smart(fun): # we can use this function to change the behaviour of inbuild function, called Decorator
    def div(a,b):
        if a<b:
            a,b = b,a
            return fun(a,b)
    return div
calc=smart(calc)
calc(3,6)