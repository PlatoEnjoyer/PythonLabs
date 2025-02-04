s = input()

d = dict()

for el in s:
    if el == ' ':
        continue
    if el in d.keys():
        d[el] += 1
    else:
        d[el] = 1


m_s = ''
m_v = 0

for el in d.keys():
    if d[el] > m_v:
        m_s = el
        m_v = d[el]

print(m_s, m_v)