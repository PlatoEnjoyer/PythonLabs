s = input()

res = ''

for i in range(len(s)):
    if s[i].isdigit():
        continue
    
    if i != len(s) - 1:
        if s[i + 1].isdigit():
            res += s[i] * int(s[i + 1])
            i += 1
        else:
            res += s[i]

if s[-1].isdigit():
    res += s[-2] * s[-1]
else:
    res += s[-1]

print(res)