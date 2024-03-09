def find_next_empty(puzzle):
    #find nexr row column on the puzzle that is not filled in yet4 --> rep with -1
    #return row, col tuple (or (None, None) if there is none)
    #we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):# range (9) is 0,1,2,3,4,5,6,7,8
            if puzzle[r][c] == -1:
                return r, c
    return None, None   #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    #figuers out wither guess at row/col is valid
    #returns True if valid, false otherwise

    #let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now let's do the column
    # col_vals=[]
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    # or
    col_vals= [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #and then the square
    #we want to get where the 3X3 square starts
    #and iterate over the 3 values in column

    row_start=(row//3)*3  
    col_start=(col//3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    #If we get here the checks pass
    return True

def solve_sudoku(puzzle):
    #solve sudokuusing backtracking!
    #our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    #return whether solution exists
    #mutates puzzle to be the solution (if it exists)

    #Step 1.0: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #Step 1.1: if there is no where left, then we're done beacause we only allowed valid inputs
    if row is None: 
        return True
    #Step2: if there is a place to put the number, then make a guess between 1 and 9
    for guess in range (1, 10): #1,2,3,4,5,6,7,8,9
        #step 3: chech if this is a valid guess
        if is_valid(puzzle, guess, row , col):
            #step 3.1: if this valid, then place the guess ont the puzzle 
            puzzle[row][col]=guess
            #now we recurese the puzzle
            #step 4 recursivvly call our function
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid OR we didn't solve the puzzle after that guess, then we need to back track and try a new number
        puzzle[row][col] = -1 # reset the guess

    #step 6:if none of the numbers work, then there is no solution 
    return False
            

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)