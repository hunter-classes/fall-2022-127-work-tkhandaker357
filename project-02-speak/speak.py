# EXTRAS COMPLETED:
# put story to be translated in input.txt, and dictionary file in dictionary.txt
# functions handle period punctuation and capitalisation

file = open('./dictionary.txt')
file2 = open('./input.txt')

wordBank : str = file.read()
stringToTranslate : str = ' ' + file2.read().lower()

def capitaliseFirstLetter(string : str) -> str:
    for index in range(len(string)):
        if string[index] != ' ':
            return string[index : ].capitalize()

def stringToDict(dictionaryFile : str, separator : str) -> dict:
    newDictionary : dict = {}
    dictFileLines : list = dictionaryFile.split(separator)
    key : str = ""; value : str = ""
    
    for i in range(len(dictFileLines)):
        key = dictFileLines[i][0 : dictFileLines[i].find(':')]
        value = dictFileLines[i][dictFileLines[i].find(':') + 1 : ]
        newDictionary[key] = value
        key = ""; value = ""

    return newDictionary

def translateStory(story : str, dictionary : dict) -> str:
    newStory : str = story
    for originalWord in dictionary:
        newStory = newStory.replace((' ' + originalWord), ' ' + dictionary[originalWord])

    if newStory.find('.') != -1:
        stringsToCapitalise : list = newStory.split('.')
        newParagraph : list = []

        for string in stringsToCapitalise:
            if len(string) > 0:
                newParagraph += [capitaliseFirstLetter(string)]

        return '. '.join(newParagraph)
    else:
        return newStory.capitalize()

print(translateStory(stringToTranslate, stringToDict(wordBank, '\n')))