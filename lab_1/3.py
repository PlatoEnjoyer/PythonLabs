from math import factorial

n = int(input())


def cnk(n, k):
    return int(factorial(n)/(factorial(n - k)*factorial(k)))

def pascal_triangle(n, lvl):
    print(' '*(n - (lvl)), end='')
    
    for k in range(lvl//2+1):
        print(cnk(lvl, k), end=' ')
    for k in range(lvl//2, -1, -1):
        if lvl % 2 == 0 and k == lvl//2:
            continue
        print(cnk(lvl, k), end=' ')
    print()

    if lvl == n:
        return
    else:
        pascal_triangle(n, lvl+1)
    

pascal_triangle(n, 0)