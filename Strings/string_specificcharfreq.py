from collections import Counter
test_list = ["Being happy is my everyday goal"]
print("The original list is :" + str(test_list))
chr_list = ['e', 'a', 'p', 'y']
res = {key:val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}
print("Specific character frequencies: " + str(res))
