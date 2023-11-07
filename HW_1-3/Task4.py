n = int(input("Enter size of list: "))

list_numbers = []

for i in range(n):
    elem = int(input())
    list_numbers.append(elem)

k = int(input("Enter rotation: "))

list_numbers.extend(list_numbers[:k])

for i in range(k):
    list_numbers.pop(0)

print(list_numbers)