s = "I am 21 years old."
l = any(c.isalpha() for c in s)
m = any(c.isdigit() for c in s)
if l and m:
    print(True)
else:
    print(False)

#another example

s1 = "I am happy"
p = any(x.isalpha() for x in s1)
q = any(x.isdigit() for x in s1)
if p and q:
    print(True)
else:
    print(False)