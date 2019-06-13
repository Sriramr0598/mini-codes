pyg = 'ay'
print "This is the Pig Translator"
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    first=original[0]
    new_word= word[1:] + first + pyg
    print new_word
else:
    print 'empty'
