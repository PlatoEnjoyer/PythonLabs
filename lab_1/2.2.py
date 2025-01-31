n = int(input())
spaces = n

def pyramide(n, spaces):
    print(' '*(spaces-n), end='')
    if n == 1:
        print(1)
        return
    
    for i in range(n, 0, -1):
        print(i, end='')
    for i in range(2, n+1):
        print(i, end='')

    print()
    pyramide(n - 1, spaces)

pyramide(n, spaces)