import array

arr = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = arr.count(2)

print("Number of occurrences of 2:", count)