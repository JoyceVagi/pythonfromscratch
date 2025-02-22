string = "I am Happy Today"
vowels = "aeiouAEIOU"

res = sum(string.count(vowel) for vowel in vowels)
print(res)