#initialize a dictionary of lists
#create an empty dictionary
d = {}
#add values to the dict
d["1"] = [1,2]
d["2"] = ["python", "is", "cool"]
print(d)

#using zip() function
k = ["fruits", "vegetables", "colors"]
val = [["apple, pear"], ["potato", "carrot"], ["white", "blue"]]
d = dict(zip(k,val)) #zip() combines the k and the val lists into pairs(tuples), and the dict converts the pairs into dictionary
print(d)


#using defaultdict from collections 
from collections import defaultdict
d = defaultdict(list) #initialize a defaultdict with lists as its default type 
#now we add values to the dict usind the append funtion 
d["1"].append("white")
d["2"].append("pink")
d["3"].append("blue")
print(d)