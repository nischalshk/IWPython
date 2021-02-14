# . Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = input('Enter n : ')

req = {}

sqr = lambda x: x * x

for i in range(int(n)):
    req[i + 1] = sqr(i + 1)

print(req)
