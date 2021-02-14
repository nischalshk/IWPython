# Write a Python program to remove duplicates from a list

def rmDuplicate(l):
    filtered = []

    for i in l:
        if i not in filtered:
            filtered.append(i)

    return filtered


print(rmDuplicate([10, 20, 20, 1]))
