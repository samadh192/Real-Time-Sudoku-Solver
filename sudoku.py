from math import sqrt
from random import shuffle

class Game:
    def __init__(self,board,size):
            self.board = board
            self.board_size = size
            self.grid_size = int(sqrt(size))
            counter = 0
            for row in board:
                for col in row:
                    counter = counter+1 if col == 0 else counter
            self.emptyCells = counter
            self.num_list_random = []
            self.num_list = []
            for num in range(1,size+1):
                self.num_list.append(num)
                self.num_list_random.append(num)
            shuffle(self.num_list_random)
    
    def printBoard(self):
        print("-"*37)
        for i, row in enumerate(self.board):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("-"*37)
            elif i % 3 == 2:
                print("|" + "---+"*8 + "---|")
            else:
                print("|" + "   +"*8 + "   |")
    
    def isValidInsertion(self,num,i,j):
        if num > 9 or num < 1:
            return False
        #getting col
        col = []
        for row in self.board:
            col.append(row[j])
        
        #getting row
        row = self.board[i]
        
        #getting sub-grid
        grid = []
        start_i = 0 if i<3 else ( 3 if i<6 else 6 )
        start_j = 0 if j<3 else ( 3 if j<6 else 6 )
        for i in range(start_i,start_i+3):
            for j in range(start_j,start_j+3):
                grid.append(self.board[i][j])

        if num not in row and num not in col and num not in grid:
            return True
        else:
            return False
    
    def setPosition(self,num,row,col):
        self.board[row][col] = num
        self.emptyCells -= 1
    
    def unsetPosition(self,row,col):
        self.board[row][col] = 0
        self.emptyCells += 1

    def getEmptyCells(self):
        return self.emptyCells

    def solve_Normal(self):
        if self.getEmptyCells() == 0:
            return True
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    continue
                for num in self.num_list:
                    if self.isValidInsertion(num,row,col):
                        self.setPosition(num,row,col)
                        if self.solve_Normal():
                            return True
                        else :
                            self.unsetPosition(row,col)
                return False
    
    def solve_Randomised(self):
        if self.getEmptyCells() == 0:
            return True
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    continue
                for num in self.num_list_random:
                    if self.isValidInsertion(num,row,col):
                        self.setPosition(num,row,col)
                        if self.solve_Randomised():
                            return True
                        else :
                            self.unsetPosition(row,col)
                return False