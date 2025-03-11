import os
path = str(os.getcwd())
print(os.path.abspath('input.txt'))
f = open('ex 1\input.txt')

l = list(map(int, f.read().split()))
f.close()

print(l)
s = 0
for el in l:
    s += el

f = open('ex 1\output.txt', 'w')
f.write(str(s))
f.close()