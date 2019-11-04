
# swap 1
a = 5
b = 6

temp = a
a = b
b = temp

# swap 2
m = 5
n = 6

m = m + n
n = m - n
m = m - n

# swap 3

x = 5
y = 6

x = x ^ y
print(x)
y = x ^ y
print(y)
x = x ^ y

# swap 4 --> best in python
p = 5
q = 6

p,q = q,p

print(a,b)
print(m,n)
print(x,y)
print(p,q)