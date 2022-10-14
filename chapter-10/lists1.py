myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList += [True, 4, 76]
print(myList)

myList += ["apple", 76]
myList.insert(3, "cat")
myList.insert(0, 99)
print(myList)

helloIndex = 0
for index in range(len(myList)):
    if myList[index] == "hello":
        helloIndex = index
        break
print(helloIndex)

seventySixCount = 0
for index in range(len(myList)):
    if myList[index] == 76:
        seventySixCount += 1
print(seventySixCount)

seventySixIndex = 0
trueIndex = 0
for index in range(len(myList)):
    if myList[index] == 76:
        seventySixIndex = index
        pass
    if myList[index] == True:
        trueIndex = index
myList.pop(seventySixIndex)
myList.pop(trueIndex)
print(myList)



