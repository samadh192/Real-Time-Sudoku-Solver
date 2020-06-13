import sudoku
from os import system, name
from time import sleep
from timeit import default_timer as timer

def clear(): #clear screen for windows and linux
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

grid = [[4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 9, 8],
        [3, 0, 0, 0, 8, 2, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 7, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 7],
        [6, 4, 0, 3, 0, 0, 0, 0, 0]]

grid_advanced = [[0, 6, 0, 4, 0 ,0, 0, 7, 0],
                 [0, 8, 0, 0, 0, 0, 0, 2, 9],
                 [0, 7, 0, 0, 2, 0, 5, 0, 0],
                 [0, 0, 5, 6, 0, 0, 0, 0, 4],
                 [9, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 5, 0, 0, 0, 0, 3],
                 [0, 0, 4, 1, 0, 0, 0, 0, 0],
                 [8, 0, 0, 0, 9, 0, 0, 0, 0],
                 [0, 0, 0, 0, 8, 0, 1, 0, 6]]


game = sudoku.Game(grid_advanced,len(grid_advanced[0]))
start = timer()
game.solve_Normal()
end = timer()
game.printBoard()
print('Normal Backtracking: ',end - start,'\n')