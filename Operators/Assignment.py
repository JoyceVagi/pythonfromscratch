#Assignment operators are used to assign the value of the right side of the expression to the left side operand.

#Addition assignment 
a = 3
b = 5
# a = a + b
a += b
print(a)

#Subtraction assignment
a = 3
b = 5
a -= b
print(a)

#Multiplication Assignment 
a = 3
b = 5
a *= b
print(a)

#Division Assignment
a = 3
b = 5
a /= b
print(a)

#Modulus Assignment: it first divides the operands and then takes the remainder and assigns it to the left operand.
a = 3
b = 5
a %= b
print(a)

#Floor Division Assignment:used to divide the left operand with the right operand and then assigs the result(floor value) to the left operand.
a = 3
b = 5
a //= b
print(a)

#Exponentiation Assignment
a = 3
b = 5
a **= b
print(a)

#Bitwise AND Assignment
a = 3
b = 5
a &= b
print(a)

#Bitwise OR Assignment
a = 3
b = 5
a |= b
print(a)

#Bitwise XOR Assignment 
a = 3
b = 5
a ^= b
print(a)

#Bitwise Right Shift Assignment
a = 3
b = 5
a >>= b
print(a)

#Bitwise Left Shift Assignment
a = 3
b = 5
a <<= b
print(a)

#Walrus Operator
#Syntax: a := expression
#The operator will solve the expression on the right-hand side and assign the value to the left-hand side operand ‘x’ and then execute the remaining code.
# a list
a = [1, 2, 3, 4, 5]

# walrus operator
while(x := len(a)) > 2:
    a.pop()
    print(x)






