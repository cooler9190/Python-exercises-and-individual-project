n = int(input("Enter a number: "))

list_numbers = []

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        list_numbers.append("FizzBuzz")
    elif i % 5 == 0:
        list_numbers.append("Buzz")
    elif i % 3 == 0:
        list_numbers.append("Fizz")
    else:
        list_numbers.append(i)

print(list_numbers)