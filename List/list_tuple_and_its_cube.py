#using list comprehension
a = [1,2,3,4,5]
res = [(n,n**3) for n in a] #[(n, n**3) for n in numbers] iterates over each element n in the list numbers.
print(res)

#for loop with append
a = [1,2,3,4,5]
res = []
for n in a:
    res.append((n,n**3))
print(res)

#using generator and list()
a = [1,2,3,4,5]
res = list((n, n**3) for n in a)
print(res)