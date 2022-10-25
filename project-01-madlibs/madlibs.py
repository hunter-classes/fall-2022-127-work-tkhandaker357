# EXTRAS COMPLETED:
# 1: Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the
#    file in your repo and that your program reads it correctly.
# 2: Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that
#    replacement.
# 3: Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise,
#    lowercase.This is except in the case of proper nouns which should always be capitalized. 

import random

file = open("story.dat")
story = file.read()
story = story.split('\n')
story = ' '.join(story)

wordBank = [
    ["<VERB>", "threw", "ran", "walked", "talked", "hit", "flew", "ate", "yelled", "jumped"],
    ["<OBJECT>", "car", "hammer", "sword", "gun", "pie", "pizza", "person", "dog", "cat"],
    ["<CHAR>", "Sam", "Bob", "Alex", "Emily", "John", "Martha", "Sock", "Kevin", "Fred"],
    ["<ADVERB>", "unceremoniously", "distraughtly", "ecstatically", "furiously", "gleefully", "flamboyantly", "idiotically", "grossly",
                "reasonably"]
]

def replaceWords(sentence):
    if "<MAINCHAR>" in sentence:
        sentence = sentence.replace("<MAINCHAR>", wordBank[2][random.randrange(1, len(wordBank[2]))])

    paragraph = sentence.split('.')
    newParagraph = []

    for sentence in paragraph:
        newSentence = sentence
        for wordType in wordBank:
            if wordType[0] in sentence:
                newSentence = newSentence.replace(wordType[0], wordType[random.randrange(1, len(wordType))])
        newParagraph.append(newSentence)
        newSentence = newSentence.capitalize()
        
    return '.'.join(newParagraph)


print(replaceWords(story))
