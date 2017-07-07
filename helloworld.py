word = 'asshole'
print (word[::-1])

def reversed(pword):
    length = len(pword)
    if(length>0 and pword!=None):
        return '{}{}'.format(pword[length-1],reversed(pword[:-1]))

rev = reversed(word)

print(rev)