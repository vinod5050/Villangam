Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 	tup = (95,6,87,1,9)
	
SyntaxError: unexpected indent
>>> tup = (95,6,87,1,9)
>>> tup
(95, 6, 87, 1, 9)
>>> tup = (45,67,89,3,6)
>>> tup
(45, 67, 89, 3, 6)
>>> tup[3]
3
>>> tup[2] =1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tup[2] =1
TypeError: 'tuple' object does not support item assignment
>>> set1 = {4,7,3,88,14}
>>> set1
{3, 4, 7, 14, 88}
>>> set1
{3, 4, 7, 14, 88}
>>> set1 = {6,89,4,90}
>>> set1
{89, 90, 4, 6}
>>> set1[2]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
>>> List is mutable, tuple is immutable and faster than list, set is like list but not in sequence order
