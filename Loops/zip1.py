#the zip() function is used to combine 2 or more values in the container sequentially, and the loop exists only till the smaller container ends
names = ['Rachel', 'Ross', 'Joey', 'Phoebe'] #list
age = (25, 28, 26)
for names, age in zip(names, age):
    print('Name:', names)
    print('Age:', age)
    print()