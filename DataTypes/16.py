# Write a Python program to sum all the items in a list.

def sumAllfromList(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(sumAllfromList([0, 1, 2, 3, 4]))
