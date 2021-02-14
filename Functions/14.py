# Write a Python program to sort a list of dictionaries using Lambda

nameSort = lambda x: x['name']

sample = [
    {
        "name": "Nischal"
    },
    {
        "name": "Shakya"
    },
    {
        "name": "Nepali"
    },
]

sorted_list = sorted(sample, key=nameSort)

print(sorted_list)
