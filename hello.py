

import csv
import random

namesList = {'Ahmad, Daanish': 0}


with open('/Users/sunnyzhao/Desktop/StudentList.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    counter = 1
    for row in csv_reader: 
            namesList.update({f'{row["Ahmad"]}, {row["Daanish"]}': counter})
            counter += 1

def shuffleNames():
    shuffledKeys = list(namesList.keys())
    random.shuffle(shuffledKeys)
    return shuffledKeys

shuffledKeys = shuffleNames()

def assign():
    counter = 0
    print('\nKitchen staff:')
    while counter <= 6:
        print(shuffledKeys.pop(0))
        counter += 1
    print('\nWaiters:')
    for waitingTable in range(31):
        print(shuffledKeys.pop(0) + f' waiting at table {counter - 6}')
        counter += 1 

    print('\nTable seatings:')

    tableNumber = 1 
    tableCounter = 1
    while tableNumber <= 31: 
        print(shuffledKeys.pop(0)+ f' sitting at table {tableNumber}')
        tableCounter += 1 
        if tableCounter % 8 == 0:
            tableNumber += 1 
    remainderTableCounter = 1 
    for name in range(5):
        print(shuffledKeys.pop(0) + f' sitting at table {remainderTableCounter}')
        remainderTableCounter += 1 

assign()









