Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num =[2,45,6,77]
>>> num
[2, 45, 6, 77]
>>> num[0]
2
>>> num[3]
77
>>> num[-1]
77
>>> num[-4]
2
>>> num[2:]
[6, 77]
>>> num[:2]
[2, 45]
>>> names=['vinod','doniv','rajesh','kanna']
>>> names
['vinod', 'doniv', 'rajesh', 'kanna']
>>> values=[3.4,'vinod',4]
>>> values
[3.4, 'vinod', 4]
>>> com = [num,names,values]
>>> com
[[2, 45, 6, 77], ['vinod', 'doniv', 'rajesh', 'kanna'], [3.4, 'vinod', 4]]
>>> num.append(22)
>>> num
[2, 45, 6, 77, 22]
>>> num.count
<built-in method count of list object at 0x03597530>
>>> num.count()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    num.count()
TypeError: count() takes exactly one argument (0 given)
>>> num.count(2)
1
>>> num.count(5)
0
>>> num.count(1)
0
>>> num.count(0)
0
>>> num.count(2)
1
>>> num.count(3)
0
>>> num.insert(2,77)
>>> num
[2, 45, 77, 6, 77, 22]
>>> num.remove(2)
>>> num
[45, 77, 6, 77, 22]
>>> num.pop(1)
77
>>> num
[45, 6, 77, 22]
>>> num.pop()
22
>>> num
[45, 6, 77]
>>> 
>>> del num[2:]
>>> num
[45, 6]
>>> num.extend([40,66,88,99)]
SyntaxError: invalid syntax
>>> num.extend([40,66,88,99])
>>> num
[45, 6, 40, 66, 88, 99]
>>> min(num)
6
>>> max(num)
99
>>> sum(num)
344
>>> num.sort()
>>> num
[6, 40, 45, 66, 88, 99]
>>> num.count()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    num.count()
TypeError: count() takes exactly one argument (0 given)
>>> 
