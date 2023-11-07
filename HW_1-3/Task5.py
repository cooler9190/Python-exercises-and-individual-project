sentence = "Hello, World!"

result = 0

vouls = ['a', 'o', 'u', 'e', 'i']

sentence = sentence.lower()

for char in sentence:
    if char.isalpha():
        for voul in vouls:
            if char == voul:
                result += 1

print(result)
