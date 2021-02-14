# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

d = input("Enter a text: ")

x = d.split(" ")

pattern1 = "poor"
pattern2 = "not"

poor = d.find(pattern1)
nott = d.find(pattern2)

if poor > -1 and nott > -1:
    start = poor if poor < nott else nott
    end = poor + 4 if poor > nott else nott + 3
    frontText = d[0:start]
    backText = d[end:]

    print(frontText + "good" + backText)
