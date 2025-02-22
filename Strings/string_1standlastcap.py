s = "happy day"
w = s.split()
res = " ".join([
    i[0].upper() + i[1:-1] + i[-1].upper()
    if len(i) > 1 else i.upper()
    for i in w
])
print(res)

s1 = "joyce vagdevi"
w1 = s1.split()
resl = ' '.join([
    i[0].upper() + i[1:-1] + i[-1].upper()
    if len(i) > 1 else i.upper()
    for i in w1
])
print(resl)

