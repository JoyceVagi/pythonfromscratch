import array as arr 
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print(a)

sliced_array = a[3:5]
print(sliced_array)

sliced_array = a[5:]
print(sliced_array)

sliced_array = a[:6]
print(sliced_array)

sliced_array = a[:]
print(sliced_array)