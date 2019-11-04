### For loop working in sequential order
x = ['Vinod', 2015, 2019]

for i in x:
    print(i)
print('####################################')
### Printing the string in sequential order
y = "Vinod"

for j in y:
    print(j)
print('####################################')
### We can use input directly in for loop
for k in 'Doniv':
    print(k)
print('####################################')
### Printing the values in range wise from 0 to 4 by using range keyword
for l in range(5):
    print(l)
print('####################################')
### Printing the value by using manualy range(0 start, 25 till,5 diff)
for m in range(0, 25, 5):
    print(m)
print('####################################')
### Printing the value by reverse order
for m in range(25, 0, -5):
    print(m)
print('####################################')
### Printing the Even value by using if condition inside for loop
for m in range(1,11):
    if m%2 == 0:
        print(m)
print('####################################')
