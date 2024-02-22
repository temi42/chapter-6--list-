ROWS= 4
COLS =4

myTable = [[65,54,95,80],
           [55,34,65,70],
           [60,50,75,85],
           [45,44,95,80]]

newTable = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

for row in range(ROWS): #LINE 1
    sum = 0 #LINE 2
    for col in range(COLS): #LINE 3
        newTable[row][col]= myTable[col][row] #LINE 4
        sum = sum + (newTable[row][col]) #LINE 5
    newTable[row][ROWS] = sum

for row in range(ROWS):
    print(newTable[row])
