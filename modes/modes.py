def findLargest(list):
    list.sort()
    return list[-1]


def frequency(list, value):
    return len([item for item in list if item == value])


def mode(list):
    frequencies = []
    for number in list:
        frequencies.append([item for item in list if item == number])

    modeIndex = 0
    for index in range(len(list)):
        if frequency(frequencies, list[index]) > modeIndex:
            modeIndex = index
    
    return frequencies[modeIndex][0]

testList = [5, 4, 3, 4, 2, 4, 10, 9, 2, 2, 2, 2, 234, 4, 9884]
print("Largest in List:", findLargest(testList))
print("Frequency of 4 in List:", frequency(testList, 4))
print("Mode of list:", mode(testList))