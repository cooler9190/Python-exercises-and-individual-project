# 10*.Lexicographic Permutations Generator
# Description: Write a generator to yield all lexicographically ordered permutations of a given string.
# Example Input: “ABC”
# Example Output: “ABC”, “ACB”, “BAC”, “BCA”, “CAB”, “CBA”

from itertools import permutations


def generate_permutations(word, i=0):
    # perms = permutations(word)
    # for perm in perms:
        # yield ''.join(word)

    if i == len(word):
        # joins elements of sequence
        print(''.join(word))

    for j in range(i, len(word)):
        perm = [c for c in word]

        # swap
        perm[i], perm[j] = perm[j], perm[i]

        yield from generate_permutations(perm, i + 1)


sentence = input("Enter a string: ")

print(*(generate_permutations(sentence)), sep=', ')
