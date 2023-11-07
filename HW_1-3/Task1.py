list_numbers = [1, 9, 6, 2, 8, 5, 3]

list_numbers.sort()

list_numbers2 = list_numbers.copy()

for i in range(len(list_numbers2)):
    list_numbers2[i] *= list_numbers2[i]

print(list_numbers)

print(list_numbers2)



