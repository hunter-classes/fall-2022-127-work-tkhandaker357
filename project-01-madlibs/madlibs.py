import random

wordBank = [
    ["<VERB>", "threw", "ran", "walked", "talked", "hit", "flew", "ate", "yelled", "jumped"],
    ["<OBJECT>", "car", "hammer", "sword", "gun", "pie", "pizza", "person", "dog", "cat"],
    ["<CHAR>", "Sam", "Bob", "Alex", "Emily", "John", "Martha", "Sock", "Kevin", "Fred"],
    ["<ADVERB>", "unceremoniously", "distraughtly", "ecstatically", "furiously", "gleefully", "flamboyantly", "idiotically", "grossly",
                "reasonably"],
    ["<PRONOUN>", "he", "she", "they"]
]


def replaceWords(sentence):
    if "<HERO>" in sentence:
        sentence = sentence.replace("<HERO>", wordBank[2][random.randrange(1, len(wordBank[2]))])

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


story = "<HERO> took the <OBJECT> and <VERB> it <ADVERB>. <HERO> then <VERB> an entire <OBJECT> at <CHAR>."
print(replaceWords(story))
