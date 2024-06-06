# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


min = 1
max = int(input("Enter the maximum number: "))

list_of_odd_numbers = []

for i in range(min, max+1):
    if i%2 == 0: list_of_odd_numbers.append(i)

print(list_of_odd_numbers)