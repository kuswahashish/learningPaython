#remove the duplicates from list
numbers = [12,11,14,25,12,26,11]
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)
print("Before removing duplicates :",numbers)
print("After  removing duplicates :",unique)