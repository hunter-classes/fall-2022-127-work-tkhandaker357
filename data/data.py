# EXTRAS COMPLETED:
# used matplotlib to plot the graph 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./classics.csv")
daysOfRelease = data.loc[:, "bibliography.publication.day"]
sortedPubDays : list = daysOfRelease.sort_values()

# is inclusive
def specificRange(startingNum : int, endingNum : int, step : int = 1) -> list:
    return range(startingNum, endingNum + 1, step)

numOfBooksPerDay : list = []
days : list = specificRange(1, 31)

for day in specificRange(1, 31):
    numOfBooks : int = 0
    for [bookNum, releaseDay] in enumerate(sortedPubDays):
        if releaseDay == day:
            numOfBooks += 1
    numOfBooksPerDay += [numOfBooks]

plt.plot(days, numOfBooksPerDay)
plt.xlabel("Days of Publication")
plt.ylabel("Number of Books Released")
plt.gcf().autofmt_xdate()
plt.show()    
