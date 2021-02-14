# Write a Python function to check whether a number is in a given range.

x = input("Enter a number : ")


# Let the range be 0 to 100

def liesInRange(n):
    if 0 <= n <= 100:
        return True
    else:
        return False


print(liesInRange(int(x)))
