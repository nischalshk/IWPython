#  Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

def checkEmptyDictionList(l):
    value = True
    for i in l:
        if bool(i):
            value = False
            break
    return value


print(checkEmptyDictionList([{}, {}, {}]))
print(checkEmptyDictionList([{1, 2}, {}, {}]))
