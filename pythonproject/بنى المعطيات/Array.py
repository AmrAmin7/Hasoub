numbers =[1,2,3,4,5]

print (numbers[2])

for x in numbers:
    print(x)

numbers.append(6)      #لإضافة عنصر للمصفوفة
for x in numbers:
    print(x)

numbers.pop(2)    #لحذف العنصر اللى فى موقع 2
for x in numbers:
    print(x)

numbers.remove(6)     #لحذف العنصر 6
for x in numbers:
    print(x)

