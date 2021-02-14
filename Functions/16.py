# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

sqr = lambda x: x ** 2
cub = lambda x: x ** 3

sample = [1, 2, 3, 4]

sqrd = list(map(sqr, sample))
cubed = list(map(cub, sample))

print(sqrd)
print(cubed)
