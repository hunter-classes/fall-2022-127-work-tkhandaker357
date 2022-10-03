import piglatin

def piglatin_sentence(sentence):
    words = sentence.split(' ')
    index = 0
    for word in words:
        words[index] = piglatin.piglatin(word)
        index += 1
    return ' '.join(words)

print(piglatin_sentence("poop poopie stinky fart fart poop poop"))   