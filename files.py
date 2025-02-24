file = open("hello.txt", "r")
# a - append | r - read | w - write | x - create
numbers = file.readlines()
total = 0
for number in numbers:
    print(number.strip())
    total += int(number)

print("Total: " + str(total))
file.close()