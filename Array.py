from array import *
# print the values in array one by one
vals = array('i',[5,7,8,3,8])
for i in vals:
    print(i)

# move the array values in one array to another array

# below  line will work
#new = vals

# below line will  move the array values with some addition operation.
new = array(vals.typecode,(a*2 for a in vals))

for j in new:
    print(j)

# get the array length and values from user
arr = array('i',[])
n = int(input('Enter the length of array :'))
for k in range(n):
    m = int(input('Enter the values :'))
    arr.append(m)
print(arr)
print(max(arr))
