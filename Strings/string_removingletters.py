s = "Hello World"
s = s.replace("H", " ")
print(s)

#using loop
s1 = " "
for c in s:
    if c != "o":
        s1 += c
print(s1)