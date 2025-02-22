s = "i am happy"
v = "aeiou"

if all(i in s.lower() for i in v):
    print(True)
else:
    print(False)

#another example 
x = "this apple is yours"
w = "aeiou"
if all(i in x.lower() for i in w):
    print(True)
else:
    print(False)