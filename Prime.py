a = int(input("starting number :"))
b = int(input("starting number :"))

for i in range(a,b):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                print('Not a prime number : ', i)
                break
        else:
            print('It\'s a prime number : ', i)
    else:
        print('Not a prime number : ', i )