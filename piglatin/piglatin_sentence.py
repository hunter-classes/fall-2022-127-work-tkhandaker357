import piglatin

def piglatin_sentence(sentence):
    words = sentence.split(' ')
    index = 0
    for word in words:
        words[index] = piglatin.piglatin(word)
        index += 1
    return ' '.join(words)

print(piglatin_sentence("I drove a honda civic over 15 kids yesterday. 36 missing, 14 found."))   