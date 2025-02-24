x = 4
y = 5
name = "ralph"
father_name = "macalino"
is_student = True
age = 25
print(name + " " + father_name + " " + str(age) + " years old")

# taking inputs for variables

name = input("Enter your name: ")
print("Hello " + name)  # concatenation


# ask user for their age, and tell them their age after 5 years

age = input("Enter your age: ")
age_after_5_years = int(age) + 5
print("Your age after 5 years will be " + str(age_after_5_years))