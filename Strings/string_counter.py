from collections import Counter
s ="GeeksforGeeks"
freq = Counter(s)
res = min(freq, key=freq.get)
res2 = max(freq, key=freq.get)
print(str(res))
print(str(res2))

