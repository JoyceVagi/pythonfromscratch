#using dict.fromkeys()
k = ['a', 'b', 'c', 'd']
val = 0
res = dict.fromkeys(k,val)
print(res)

#using a for loop
k = ['a','b','c','d']
val = 0
res = {}
for n in k:
    res[n] = val
print(res)