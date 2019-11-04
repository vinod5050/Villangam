from numpy import *

a1 = array([1,2,3,4,5])
print(id(a1))
a2 = array([6,7,8,9,10])
a = a1 + a2
print(a)

a += 10
print(a)
print(sum(a))
print(concatenate([a1,a2]))
### copying array with different addrest
## view() --shallow copy( if i am changing parent array value in any place it will change for child as well )and
# copy() --deep copy(changing the array value after copy it will not reflect in child).

a3 = a1.view()
a4 = a1.copy()
a1[4] = 10
print(a1)
print(a3)
print(a4)
print(id(a1))
print(id(a3))
print(id(a4))
