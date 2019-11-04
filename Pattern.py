
for i in range(0,4):
    for j in range(i+1):
        print('#', end=' ')
    print()
## alter code
#for i in range(1,5):
#       print('# ' * i)
##
for i in range(0,4):
    for j in range(4-i):
        print('#', end=' ')
    print()
## alter code
#for i in range(4,0,-1):
#       print('# ' * i)
##
for i in range(0,4):
    for j in range(4-i):
        print(i+j+1, end=' ')
    print()

x='ABCD'
y='PQR'
for i in range(1,5):
	print(x[:i]+y[i-1:])

### For-Else loop( i want to print divisible of 5, if not print else part)

num = [12,14,51,79]

for i in num:
    if i % 5 == 0:
        print(i)
        break
else:
    print('not found')