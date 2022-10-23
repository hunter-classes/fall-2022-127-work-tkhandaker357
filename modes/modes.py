def findLargest(list):
    list.sort()
    return list[-1]


def freq(list, value):
    frequencyOfVal = 0
    for item in list:
        if value == item:
            frequencyOfVal += 1
    
    return frequencyOfVal


testList = [5, 4, 3, 4, 2, 4, 10, 9, 234, 4, 9884]
print("Largest in List:", findLargest(testList))
print("Frequency of 4 in List:", freq(testList, 4))
