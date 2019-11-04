### Break --> it will break the process and goes to end of the loop
x = int(input('value :'))

for i in range(0,x):

    if i >= 5:
        print('out of stock :', x - 5 )
        break
    print('Vinod')

### Continue --> It will skip the current process and again check the loop till the end of the condition

for j in range(1,20):
    if j % 3 == 0:
        continue
    print(j)

### Pass --> just pass the condition... omiting the "if" condition error
for k in range(1,20):
    if k % 2 != 0:
        pass
    else:
        print(k)
