'''def count_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count


print(count_vowels("Sara"))
print(count_vowels("HELLO"))
print(count_vowels("Python"))'''

def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found = {}

    for letter in word:
        if letter in vowels:
            found.setdefault(letter, 0)
            found[letter] += 1

    return found


print(count_vowels("Education"))
print(count_vowels("HELLO"))
print(count_vowels("Python"))