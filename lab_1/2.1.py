'''
Напишите программу, в которой задается  натуральное число n и 
выводится обратная лестница из n ступенек, i-я ступенька должна 
состоять из чисел от 1 до i без пробелов.
'''

n = int(input())

def triangle(n):
    if n == 0:
        return
    else:
        for i in range(1, n+1):
            print(i,end='')
        print()
        triangle(n - 1)

triangle(n)