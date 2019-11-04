# position argument in function.... (x,y) - formal argument....(5,6) - actual argument
def add(x, y):
    c = x + y
    return c


def add_sub(x, y):
    d = x + y
    e = x - y
    return d, e


result = add(5, 6)
# returing 2 values as d,e, so we need to accept 2 values as result1 and result2
result1, result2 = add_sub(5, 6)
print(result, result1, result2)


###################################################################################################
def update(lst):
    lst[1] = 0
    print(lst)


lst = [1, 2, 3, 4, 5]
print(lst)
update(lst)
print(lst)


###################################################################################################
# Keyword argument

def student(name, age):
    print(name, age)


student(age=25, name='vinod')


# Keyword argument
def stu(name, age=18):
    print(name, age)


stu('vinod')
stu('vinod', 15)


# Variable argument

def calc(*a):
    c = 0
    for i in a:
        c = c + i
    print(c)
calc(1, 2, 3)

#Keyword Variable argument

def per(**data):
    for i,j in data.items():
        print(i,j)
per(name='vinod',age=25,city='chennai',state='Tamil Nadu')
# Global Variable -- we can't use local var(in function var) in outside, we can use global var in fuction by using global keyword

a = 10
def no():
#    global a
    a=4
    x=globals()['a'] # we can use "global a"
    print(x)
no()
print(a)

# Passing list to function
def lists(lsts):
    even = 0
    odd = 0
    for i in lsts:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd
lsts=[1,2,3,4,5,6,7,8,9]
even,odd=lists(lsts)
print("Even : {} and Odd : {}".format(even,odd))

# Fibonacci series
print("[Fibonacci series]")
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
fib(100)
print()

# Factorial -- 5! = 5*4*3*2*1
def fact(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    print(x)
n = 8
fact(n)

# Factorial by using recursion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
n = 8
x=fact(n)
print(x)
# Anonymous/Lambda function -- any fuction have 1 statement, we can use lambda
f =lambda a : a* a
f1 = f(5)
print(f1)

h = lambda a,b : a*b
h1 = h(5,6)
print(h1)

nums = [1,2,3,4,5,6]
evens = list(filter(lambda n : n%2 == 0,nums))
print(evens, len(evens))

multi = list(map(lambda n : n*n,evens))
print(multi)

from functools import*
sum = reduce(lambda a,b: a+b,multi)
print(sum)


