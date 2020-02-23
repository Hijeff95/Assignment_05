
#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# JHsu, 2020-Feb-20, Created File
# JHsu, 2020-Feb-20, Finished File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
DicRow = {}  # list of data row
lstTbl = []  # list of lists to hold data
lstRow = []
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[1] load Inventory from file\n[2] Add CD\n[3] Display Current Inventory')
    print('[4] delete CD from Inventory\n[5] Save Inventory to file\n[x] exit')
    strChoice = input('1, 2, 3, 4, 5 or x: ')
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == '1':
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            DicRow = {'ID': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist Name': lstRow[2]}
            lstTbl.append(DicRow)
            for row in lstTbl:
                print(*row.values(), sep = ', ')
        objFile.close()
               
        pass
    
    elif strChoice == '2':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        DicRow = {'ID': intID, 'CD Title': strTitle, 'Artist Name': strArtist}
        lstTbl.append(DicRow)
        
    elif strChoice == '3':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')


    elif strChoice == '4':
        
        delEntry = input('Enter ID to delete:')
        for i in range(len(lstTbl)):
            if lstTbl[i]:       
                ['ID'] == int(delEntry)
                del lstTbl[i]
              
                print('Entry deleted')
            else:
                    print('Entry could not be deleted')
                    break
        # TODO Add functionality of deleting an entry
        pass


    elif strChoice == '5':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either 1, 2, 3, 4, 5 or x!')