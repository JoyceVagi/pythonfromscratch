"""iterating in a list"""
li = ["happy", "day", "today"]
for i in li: 
    """iterates through the values in the list"""
    print(i)
    
"""iterating in a tuple"""
tup = ("good", "day","coding")
for i in tup:
    print(i)
    
"""iterating through a variable containing a word"""
s = "Python"
for i in s:
    print(i)
    
"""iterating through dictionary"""
d = dict({'brave':1, 'smart':2})
for i in d:
    print("%s %d" % (i, d[i]))
    
"""iterating through sets"""
set1 = {1, 2, 3, 4, 5}
for i in set1:
    print(i)   