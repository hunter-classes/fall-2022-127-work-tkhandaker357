from symbol import testlist

def maxOf(list):
    list.sort()
    return list[-1]

def sumOfEvens(list):
    sum = 0
    for number in list:
        sum += number if number % 2 == 0 else 0
    return sum

def sumOfNegatives(list):
    sum = 0
    for number in list:
        sum += number if number < 0 else 0
    return sum

testList = [5, 6, 2, 8, 12, -9]
print(maxOf(testList))
print(sumOfEvens(testList))
print(sumOfNegatives(testList))