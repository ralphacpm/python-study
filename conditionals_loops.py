age = 19

if age >= 20:
    print("You are older than 20")
else:
    print("You are younger than 20")


#types of loops in python
num = 0
# while loop
while num < 10:
    print(num)
    num += 1


num = 0
# for loop
for num in range(10):
    print(num)
    num += 1

#guessing game
random_number = 5

guess = 0

while guess != random_number:
    guess = int(input("Enter your guess: "))
    if guess < random_number:
        print("Your guess is too low")
    elif guess > random_number:
        print("Your guess is too high")