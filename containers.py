name = ["Ralph", "Macalino"]
numbers = [1,2,3,4,5]
combined = ["Ralph", "Macalino", 1, 2, 3, 4, 5]

for item in combined:
    print(item)

numbers.append(6)
print(numbers)

numbers.insert(1,100)
print(numbers)

numbers.extend([7,8,9])
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.remove(100)
print(numbers)



alphaNum = {
    "One": 1,
    "Two": 2,
    "Three": 3
}

print(alphaNum["One"])
print(alphaNum["Two"])
print(alphaNum["Three"])      

for key in alphaNum.keys():
    print(alphaNum[key])


coordinates = (4, 5)
coordinates[0] = 10 