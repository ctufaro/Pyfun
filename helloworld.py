"""This module does blah blah."""

kevin = 0
stuart = 0
word = 'BANANA'
vowels = ['A', 'E', 'I', 'O', 'U']

for i in range(len(word)):
    if word[i] in vowels:
        stuart += len(word) - i
    else:
        kevin += len(word) - i

print (stuart)
print (kevin)


