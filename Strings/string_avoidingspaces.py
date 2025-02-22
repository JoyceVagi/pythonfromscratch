s = "Hello World"
s = len(s.replace(" ",""))
print(s)

#using loop
s1 = "Hi Joyce"
res = 0
for c in s1:
    if c != " ":
        res += 1
print(res)

#using list comprehension

s2 = "Hi Joyce"
s2 = len([c for c in s2 if c != " "])
print(s2)

#using regular expression
import re
s="Hello World"
res = len(re.sub(r" ", "", s))
print(res)
