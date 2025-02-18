"""nested loops are basically loops within loops, we can put anyother loop within any other type of loop"""
for i in range(1,5):
    for j in range(i):
        print(i, end = ' ')
    print()