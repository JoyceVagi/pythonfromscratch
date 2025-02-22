test_string = "iamhappy"
print("The original string is:" + str(test_string))
hlf_idx = len(test_string)//2
s = ''
for i in range(len(test_string)):
    if i >= hlf_idx:
        s += test_string[i].upper()
    else:
        s += test_string[i]
print("The result string is:", str(s))

#using slicing
tst_str = "heyjoyce"
print("The original string is:", str(tst_str))
hlf_str = len(tst_str)//2
s = tst_str[:hlf_str] + tst_str[hlf_str:].upper()
print("The resultant string is:", str(s))