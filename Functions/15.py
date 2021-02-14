# Write a Python program to filter a list of integers using Lambda.

getNumbers = lambda x: isinstance(x, int)

sample = ["Hi", 0, 9, "There", 10]

res = list(filter(getNumbers, sample))

print(res)
