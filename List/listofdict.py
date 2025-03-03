#direct method
a = [{1:"apple", 2:"pear", 3:"cherry"}, {4:"Amanda",5:"Jake", 6:"Paul"}] #here we have created a list of two dictionaries.
print(a)
print(type(a))

#using for loop, we can dynamically generate dictionaries

a = []#create an empty list
for i in range(3):
    a.append({"name":f"person{i+1}", "age":20+i})
print(a)

#using list comprehension
a = [{"name":f"person{i+1}", "age":20+i} for i in range(3)]
print(a)

    