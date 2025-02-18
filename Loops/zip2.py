#zip with same datatype
#refer zip1 for zip explaination 
question = ["name", "color", "shape"]
answer = ["apple", "red", "circle"]

for question, answer in zip(question, answer):
    print("What is your {0}? I am {1}." .format(question, answer))