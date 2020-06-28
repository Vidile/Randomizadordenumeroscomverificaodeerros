import random
random.randint(1,10)


def rand_num(low,high,n):

    for i in range(high):
        yield random.randint(low,high)

try:
    a = int(input('insira um low: '))
    b = int(input('insira um high: '))
    c = int(input('insira um n: '))

    for num in rand_num (a,b,c):
        print (num)
        
except ValueError:
    print('Tente de novo!!!')
    
