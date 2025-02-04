s = input()

res = ''
count = 0
curr = s[0]

for el in s:
    if el == curr:
        count += 1
    else:
        if count == 1:
            res += f"{curr}"
        else:
            res += f"{curr}{count}"
        curr = el
        count = 1

if count == 1:
    res += f"{curr}"
else:
    res += f"{curr}{count}"

print(res)
