from cs50 import get_int



while  True:
    n = get_int('height: ')
    if n >0 and n <=8:
        break

for i in range(n):
    print(' ' * (n-i-1),end='')
    print('#' * (i + 1),end='')
    print('  ',end='')
    print('#'* (i+1))
        

    


