from cgi import test

def smallestNumber(list):
    smallestNum = list[0]
    for number in list:
        if number < smallestNum:
            smallestNum = number
    return smallestNum

def oddList(list):
    oddList = []
    for number in list:
        if not number % 2 == 0:
            oddList.append(number)
    return oddList

def capitalizeWords(string):
    words = string.split(' ')
    for index in range(len(words)):
        words[index] = words[index].capitalize()
    return ' '.join(words)

def fiveCharUpper(string):
    words = string.split(' ')
    for index in range(len(words)):
        if len(words[index]) > 5:
            words[index] = words[index].upper()          
    return ' '.join(words)

def fiveCharInSentence(string):
    moreThanFive = 0
    words = string.split(' ')
    for index in range(len(words)):
        if (len(words[index]) > 5):
            moreThanFive += 1
    return moreThanFive

def squareNumbers(list):
    for index in range(len(list)):
        list[index] = list[index] ** 2
    return list

def addLists(list1, list2):
    newList = []
    for index in range((len(list1) if len(list1) <= len(list2) else len(list2))):
        newList.append(list1[index] + list2[index])
    return newList

def sumToEven(list):
    evenNumberIndex = 0
    sum = 0
    for index in range(len(list)):
        if list[index] % 2 == 0:
            evenNumberIndex = index
    for index in range(evenNumberIndex):
        sum += list[index]
    return sum 

def wordsUpToSam(string):
    wordsUpToSam = 0
    samIndex = 0
    words = string.split(' ')
    for index in range(len(words)):
        if words[index].find("sam"):
            samIndex = index        
    return samIndex

testList = [6, 5, 4, 3]
testList2 = [11, 15, 14, 34]
testString = "your mother smells of elderberries"
testString2 = "I hate salmon so goddamn much, why the hell did Sam give me this crap wtf..."

print(smallestNumber(testList))
print(oddList(testList))
print(capitalizeWords(testString))
print(fiveCharUpper(testString))
print(fiveCharInSentence(testString))
print(squareNumbers(testList))
print(addLists(testList, testList2))
print(sumToEven(testList2))
print(wordsUpToSam(testString2))