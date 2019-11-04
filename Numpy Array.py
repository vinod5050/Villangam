from numpy import *
### Normal Array it can use int and float values in same array
arr =array([1,3,4,5.1],int)
print(arr)

### linspace array will dive the values from and to (2 -- star, 10 -- end, 5 -- no of part(if not declare it will take 50 parts by default)
a = linspace(2,10,5)
print(a)

## arange array --> (1 --start, 10 -- till, 2 -- +2 from start)
b = arange(1,10,2)
print(b)

### logspace --> starting from 1*(if 5 -- 10000).....(5 -- 100000, 11 -- 100000000000, 3 - dividing into 3 part)
c = logspace(5,11,3)
###  '%.2f' is display 2 digit after point -- exp - 10.20
print('%.2f' %c[0])

### zeros array --> It creates a array with no of zeros in "float" format, we can change it into "int"
d = zeros(5)
print(d)

### ones array --> It creates a array with no of ones in "float" format, we can change it into "int"
e = ones(5)
print(e)