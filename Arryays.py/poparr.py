"""removing elements from an array: remove(), pop()"""
import array as arr 

a = arr.array('i',[1, 2, 3, 4, 5])
a.remove(2)
print(a)
"""removing the 2nd occurance of the array"""
a.pop(3)
print(a)
"""removing the 3rd occurance of the array"""