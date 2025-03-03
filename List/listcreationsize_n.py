#creating list of size n
n = 5
a = [0] * n
print(a)

#using list comprehension
n = 7
a = [0 for i in range(n)]
print(a)

#using list constructor with range()
n = 3
a = list(range(n))
print(a)

#using for loop
n = 4
a = []#initialize an empty list
for i in range(n):
    a.append(1)
print(a)

