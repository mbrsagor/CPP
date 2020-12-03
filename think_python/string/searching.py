def find(word, letter):
    index = 0

    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


f_word = "Mbr-Sagor"
f_letter = 'S'
print(find(f_word, f_letter))

print("\n")


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)


in_both('apples', 'oranges')
