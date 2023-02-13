import contextlib

global rows
global columns


class Cell:

    def __init__(self):
        self.valid_numbers = [1,2,3,4,5,6,7,8,9] 

    def __repr__(self):
        return "Node: %s" % id(self)
    
    def getNumbers(self):
        return self.valid_numbers

    def getValue(self, i):
        return int(self.valid_numbers[i])

    def getRow(self, x):
        values=len(self.valid_numbers) 
        rowPrint = ""
        
        if(x==0):
            if(values>=3):
                rowPrint = "| " + str(self.valid_numbers[0]) + "," + str(self.valid_numbers[1]) + "," +str(self.valid_numbers[2]) + " "
            elif(values>=2):
                rowPrint = "| " + str(self.valid_numbers[0]) + "," + str(self.valid_numbers[1]) + "   "
            elif(values>=1):
                rowPrint = "| " + str(self.valid_numbers[0]) + "     "           
        if(x==1):
            if(values>=6):
                rowPrint = "| " + str(self.valid_numbers[3]) + "," + str(self.valid_numbers[4]) + "," +str(self.valid_numbers[5]) + " "
            elif(values>=5):
                rowPrint = "| " + str(self.valid_numbers[3]) + "," + str(self.valid_numbers[4]) + "   "
            elif(values>=4):
                rowPrint = "| " + str(self.valid_numbers[3]) + "     " 
            else:
                rowPrint = "|       "          
        if(x==2):
            if(values==9):
                rowPrint = "| " + str(self.valid_numbers[6]) + "," + str(self.valid_numbers[7]) + "," +str(self.valid_numbers[8]) + " "
            elif(values>=8):
                rowPrint = "| " + str(self.valid_numbers[6]) + "," + str(self.valid_numbers[7]) + "   "
            elif(values>=7):
                rowPrint = "| " + str(self.valid_numbers[6]) + "     "  
            else:
                rowPrint = "|       "         
        return rowPrint

    def removeNumber(self,i):
        before = len(self.valid_numbers)
        with contextlib.suppress(ValueError):
            self.valid_numbers.remove(i)
        after = len(self.valid_numbers)

        if(before != after and after >=1):
            return True
        else:
            return False


    def setNumber(self,i):
        self.valid_numbers.clear()
        self.valid_numbers.append(i)


class board:
    
    def __init__(self):
        self.cells = [[Cell() for j in range(columns)] for i in range(rows)]


    def removeValue(self,x,y,value):
        return self.cells[x][y].removeNumber(value)

    def setValue(self,x,y,value):
        xOffset = 0
        yOffset = 0
        dirtyFlag = False    
        # remove value from columns
        for i in range(rows):
            if(self.removeValue(x,i,value) == True):
                dirtyFlag = True
        # remove value from rows
        for j in range(columns):
            if(self.removeValue(j,y,value) == True):
                dirtyFlag = True
        # remove number from sub matrix
        if(x >= 6):
            xOffset = 6
        elif(x >= 3):
            xOffset = 3
        if(y >= 6):
            yOffset = 6
        elif(y >= 3):
            yOffset =3

        for i in range(int(rows/3)):
            for j in range(int(columns/3)):
                if(self.removeValue(i+xOffset, j+yOffset, value) == True):
                    dirtyFlag = True
        
        # set number to cell
        self.cells[x][y].setNumber(value)
        return dirtyFlag
 
    def printBoard(self):
        for i in range(rows):
            if((i%3)==0):
                print("=============================================================================")
            else:
                print("-----------------------------------------------------------------------------")
            for x in range(3):
                for j in range(columns):
                    if((j%3)==0):
                        print("|", end="")
                    values = self.cells[i][j].getRow(x)
                    print(values, end="")
                    if(j==columns-1):
                        print("|", end="")
                print("|")
        if(i==rows-1):
            print("=============================================================================")  
        else:
            print("-----------------------------------------------------------------------------")

    def fixBoard(self):
        dirtyFlag = False

        for i in range(rows):
            for j in range(columns):
                if(len(self.cells[i][j].getNumbers()) == 1):
                    value = self.cells[i][j].getValue(0)
                    if(self.setValue(i,j,value) == True):
                        dirtyFlag=True
        return dirtyFlag

if __name__ == "__main__":
    rows=9
    columns=9
    xcord = 0
    ycode = 0
    value = 0
    dirtyFlag = False
 
    sudoku_board = board()
    
    sudoku_board.printBoard()

    while(rows==9):
        xcord = int(input("Xcord [0-8]:"))
        ycord = int(input("YCord [0-8]:"))
        value = int(input("Value [1-9]:"))
        if(value > 0):
            dirtyFlag = sudoku_board.setValue(xcord,ycord,value)
        elif(value < 0):
            dirtyFlag = sudoku_board.removeValue(xcord,ycord,abs(value))
        
        while(dirtyFlag==True):
            print("Fixing Board")
            sudoku_board.printBoard()
            dirtyFlag = sudoku_board.fixBoard()
        print("")
        sudoku_board.printBoard()