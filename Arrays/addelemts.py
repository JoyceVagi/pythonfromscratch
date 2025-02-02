"""adding elements into the array"""
import array as arr 

a = arr.array('i',[1, 2, 3])
print("Array before insertion of element:", *a)

a.insert(1,4)
"""instering 4 at the first index"""

print("Array after insertion:", *a)
