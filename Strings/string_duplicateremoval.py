from collections import OrderedDict

def removeDupWithoutOrder(str):
    return " ".join(set(str))
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))
if __name__ == "__main__":
    str = "Iamhappy"
    print("Without order:" ,removeDupWithoutOrder(str))
    print("With Order:", removeDupWithOrder(str))



from collections import OrderedDict

def removeDupWithoutOrder(str):
    return "".join(set(str))
def removeDupWithOrder(str):
    return "".join(set(str))

if __name__ == "__main__":
    str = "GeeKforGeeKs"
    print("without order:", removeDupWithoutOrder(str))
    print("with order:", removeDupWithOrder(str))

