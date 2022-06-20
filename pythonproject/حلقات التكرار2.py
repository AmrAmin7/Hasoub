from tokenize import Number


numbers =[2,9,11,24,30,33,56,79,85,102]
newNumbers =[]
for number in numbers :
    if number >30:
        newNumbers.append(number)
print(newNumbers)
newNumbers=[number for number in numbers if number>30]
print(newNumbers)


fruits=['apple','orange','grapes','banana']
Fruits =[]
for fruit in fruits:
    Fruits.append(fruit.title())
print(Fruits)
Fruits=[fruit.title() for fruit in fruits]
print(Fruits)
