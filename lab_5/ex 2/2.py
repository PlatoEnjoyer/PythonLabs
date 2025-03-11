f = open('ex 2/input.txt')
l = sorted(list(map(int, f.read().split())))
f.close()

f = open('ex 2/output.txt', 'w')
for el in l:
    f.write(str(el) + '\n')
f.close()
