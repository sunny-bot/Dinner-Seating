import csv
import random

alphabeticalList = ['Ahmad, Daanish']

# read the namelist.csv
with open('/Users/sunnyzhao/Desktop/StudentList.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
            #add alphabeticalList entries
            alphabeticalList.append(f'{row["Ahmad"]}, {row["Daanish"]}') 
            # Dannish has given me permission to use his name in my code and agreed that this isn't a privacy violation. 
                                    
                                    
#shuffle any given list using a shallow copy to keep the objects the same
def shuffleObjects(copiedList):
    shuffledObjects = copiedList.copy()
    random.shuffle(shuffledObjects)
    return shuffledObjects

shuffledNames = shuffleObjects(alphabeticalList)

listOfTableLists = list()
temporaryList = list()
for i in range(7):
    temporaryList.append(shuffledNames.pop(0))
copiedList = temporaryList.copy()
listOfTableLists.append(copiedList)
temporaryList.clear()
for i in range(31):
    temporaryList.append(shuffledNames.pop(0))
copiedListTwo = temporaryList.copy()
listOfTableLists.append(copiedListTwo)
temporaryList.clear()
for i in range(4):
    for i in range (9):
        temporaryList.append(shuffledNames.pop(0))
    copiedListThree = temporaryList.copy()
    listOfTableLists.append(copiedListThree)
    temporaryList.clear()
for i in range(27):
    for i in range (8):
        temporaryList.append(shuffledNames.pop(0))
    copiedListFour = temporaryList.copy()
    listOfTableLists.append(copiedListFour)
    temporaryList.clear()

def printAssignments(listOfTableLists):
    print('\nKitchen Staff:')
    for i in listOfTableLists[0]:
        print(f'{i} is in the kitchen')


    print('\nWaiters:')
    waitingCounter = 1
    for i in listOfTableLists[1]:
        print(f'{i} is waiting at table {waitingCounter}')
        waitingCounter += 1

    print('\nTables:')
    for i in range(1,32):
        for name in listOfTableLists[i+1]:
            print(f'{name} is sitting at table {i}')

def shuffle(listOfTableLists):
    #disperse old kitchen crew
    for i in range(7):
        listOfTableLists[i+1].append(listOfTableLists[0].pop(0))
    #disperse old waiters
    for i in range(31):
        listOfTableLists[i+2].append(listOfTableLists[1].pop(0))
    #add new waiters
    for i in range(23):
        listOfTableLists[1].append(listOfTableLists[i+2].pop(0))
    #disperse tables 1-4
    for i in range(4):
        for x in range(8):
            listOfTableLists[i+x+3].append(listOfTableLists[i+2].pop(0))
    #disperse tables 5-24
    for i in range(20):
        for t in range(7):
            listOfTableLists[i+t+7].append(listOfTableLists[i+6].pop(0))
    #disperse tables 25-31
    for i in range(7):
        for t in range(8):
            if i+t+27 > 32:
                x = i - 33
            else:
                x = i
            listOfTableLists[x+t+27].append(listOfTableLists[i+26].pop(0))
    
#print the following onto the terminal
print('First seating assignment:')
printAssignments(listOfTableLists)

shuffle(listOfTableLists)

print('\nSecond seating assignment:')
printAssignments(listOfTableLists)

shuffle(listOfTableLists)

print('\nThird seating assignment:')
printAssignments(listOfTableLists)











