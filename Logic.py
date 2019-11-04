print("From", __name__) # it is telling the module name when we are calling this module.
# Fibonacci series
def fib(n):
    a,b,c = 0,1,0
    if a < n:
        print(a,end=" ")
        if b < n: # customer want more than 1 number
            print(b,end=' ')
            for i in range(2,n):
                c = a + b
                if c <= n:
                    print(c, end= " ")
                    a, b = b, c
                else:
                    break
    else:
        print("Entered value is invalid :", n)
# Factorial by using recursion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
# adding multiple values
def calc(*a):
    c = 0
    for i in a:
        c = c + i
    print(c)

if __name__ == "__main__": # this will work when i am running this module... if i am calling this module, it will ignore.
    calc(5,6)
    fib(11)
    print()
    x=fact(10)
    print(x)