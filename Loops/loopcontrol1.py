""" loop control statements basically change execution from their normal statements"""
"""1. CONTINUE STATEMENT"""
for letter in 'iamhappy':
    if letter == 'a' or letter == 'p':
        continue
    """here the continue statement basically skips out the letters a and p while the loop iterates through all the letters of the phrase"""
    print("Current Letter:", letter)