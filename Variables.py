Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('c:\doc\navin')
c:\doc
avin
>>> print (r'c:\doc\navin')
c:\doc\navin
>>> 
>>> 2+3
5
>>> x =2
>>> y=3
>>> x+y
5
>>> x+10
12
>>> x=5
>>> x=y
>>> x+y
6
>>> x=5
>>> x+y
8
>>> z
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> 
>>> x+y
8
>>> _+y
11
>>> _+x
16
>>> a = 'vinod'
>>> a + ' kumar'
'vinod kumar'
>>> a ' kumar'
SyntaxError: invalid syntax
>>> a[0]
'v'
>>> a[4]
'd'
>>> a[-1]
'd'
>>> a[-5]
'v'
>>> v[5]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    v[5]
NameError: name 'v' is not defined
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> 
>>> 
>>> a[:4]
'vino'
>>> a[:5]
'vinod'
>>> a[2:]
'nod'
>>> a[1:3]
'in'
>>> a[1:55]
'inod'
>>> 
>>> 
>>> a[0] = 'd'
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a[0] = 'd'
TypeError: 'str' object does not support item assignment
>>> 'd' + a[1:]
'dinod'
>>> b = _
>>> b
'dinod'
>>> len(b)
5
>>> 
