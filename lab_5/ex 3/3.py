f = open('ex 3/input.txt', encoding='utf-8')
mx = ''
mn = ''

for line in f:
    if not mx:
        mx = line
        mn = line
    else:
        if int(mx[-2]) < int(line[-2]):
            mx = line
        if int(mn[-2]) > int(line[-2]):
            mn = line
f.close()

f = open('ex 3/output_max.txt', 'w', encoding='utf-8')
f.write(mx)
f.close()

f = open('ex 3/output_min.txt', 'w', encoding='utf-8')
f.write(mn)
f.close()

