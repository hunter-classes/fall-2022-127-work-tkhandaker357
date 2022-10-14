from cgi import test


def averageOf(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)

def sumOfSquares(list):
    sum = 0
    for number in list:
        sum += (number ** 2)
    return sum

testList = [3, 4, 5, 6]
print(averageOf(testList))
print(sumOfSquares(testList))