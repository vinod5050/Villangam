Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num =10
>>> name = 'vinod'
>>> num1 = 10
>>> id(num)
1741317440
>>> id(num1)
1741317440
>>> id(name)
56584416
>>> PI =3.14
>>> PI
3.14
>>> type(PI)
<class 'float'>
>>> type(num)
<class 'int'>
>>> type(name)
<class 'str'>
>>> num2 = 2.5
>>> type(num2)
<class 'float'>
>>> num3 = 5+4j
>>> type(num3)
<class 'complex'>
>>> num3
(5+4j)
>>> a =4.3
>>> b = int(4)
>>> b
4
>>> c = float(b)
>>> c
4.0
>>> d = complex(b,c)
>>> d
(4+4j)
>>> d = complex(b,a)
>>> d
(4+4.3j)
>>> a>b
True
>>> a<b
False
>>> bool
<class 'bool'>
>>> bool = a>b
>>> bool
True
>>> int (true)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int (true)
NameError: name 'true' is not defined
>>> int (True)
1
>>> int (False)
0
>>> 
bool = a>b
>>> a>b
True
>>> 
>>> lst = [3,5,56,4]
>>> type(lst)
<class 'list'>
>>> s = {5,56,8,98)
SyntaxError: invalid syntax
>>> s = {5,56,8,98}
>>> type(s)
<class 'set'>
>>> tup = (5,56,8,98)
>>> type(tup)
<class 'tuple'>
>>> range(0,10)
range(0, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> list(range(1,10,2))
[1, 3, 5, 7, 9]
>>> type(range(10))
<class 'range'>
>>> s ={5,8,9,7,5,8}
>>> s
{8, 9, 5, 7}
>>> d = {'vinod':'infy','doniv':'tcs','rajesh':'ibm','vinod':'tcs'}
>>> d
{'vinod': 'tcs', 'doniv': 'tcs', 'rajesh': 'ibm'}
>>> d.keys()
dict_keys(['vinod', 'doniv', 'rajesh'])
>>> d.values()
dict_values(['tcs', 'tcs', 'ibm'])
>>> d = {'vinod':'infy','doniv':'tcs','rajesh':'ibm'}
>>> d
{'vinod': 'infy', 'doniv': 'tcs', 'rajesh': 'ibm'}
>>> d.keys()
dict_keys(['vinod', 'doniv', 'rajesh'])
>>> d.values()
dict_values(['infy', 'tcs', 'ibm'])
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 arguments, got 0
>>> d.get('vinod')
'infy'
>>> d['vinod]
  
SyntaxError: EOL while scanning string literal
>>> d['vinod']
'infy'
>>> d.fromkeys()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> 
