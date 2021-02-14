# . Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result

addFifteen = lambda x: x + 15

addNum = lambda x, y: x + y

MultiplyNum = lambda x, y: x * y
print(addNum(1, 2))
print(MultiplyNum(2, 2))
