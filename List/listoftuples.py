#creating a list of tuples

#using the zip() function
n = [1, 2, 3]
val = ["orange", "cherry", "blueberry"]
li = list(zip(n,val)) #zip pairs the elements from lists n and val into tuples
print(li)

#map() is the most efficient function that converts a list o lists into a list of tuples, it does so by applying the tuple constructor 
a = [["fruit", "apple"], ["veggie","carrot"], ["drink","juice"]]
res = list(map(tuple,a))
print(res)

#using list coomprehension
a = [1,2,3]
b = ["track", "basketball","soccer"]
li = [(x,y) for x, y in zip(a,b)]
print(li)