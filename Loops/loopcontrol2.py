"""2. BREAK STATEMENT"""
for letter in 'happydays':
    if letter == 'p' or letter == 'y':
        break
    """the break statement completely end the loop once it reaches iterating either p or y"""
    print("Current Letters:", letter)