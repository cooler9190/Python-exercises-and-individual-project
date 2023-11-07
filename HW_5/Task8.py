# 8.Custom ZIP Function
# Description: Implement a generator that behaves like the built-in zip function,
# taking two or more iterables and returning tuples.
# Example Input: [1, 2], [3, 4]
# Example Output: (1, 3), (2, 4)

inputLists = input("Enter lists: ")

listOfLists = []

for val in inputLists.split('], ['):
    val = val.replace('[', '').replace(']', '')
    listOfLists.append(list(val.split(', ')))


def custom_zip(iterables):
    min_length = min(len(iterable) for iterable in iterables)

    for i in range(min_length):
        yield tuple(iterable[i] for iterable in iterables)


print(*tuple(custom_zip(listOfLists)), sep=', ')
