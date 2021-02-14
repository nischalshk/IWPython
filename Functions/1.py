# Write a Python function to find the Max of three numbers.

def maximum(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c


print(maximum(110, 20, 3))
