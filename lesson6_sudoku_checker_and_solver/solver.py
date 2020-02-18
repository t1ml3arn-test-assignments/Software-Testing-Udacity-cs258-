# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

from check import check_sudoku
import itertools
import time

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
easy_solved = \
        [[2, 9, 4, 5, 6, 3, 1, 7, 8], 
        [3, 1, 6, 7, 2, 8, 4, 9, 5], 
        [8, 5, 7, 1, 4, 9, 6, 3, 2], 
        [6, 2, 9, 4, 3, 1, 5, 8, 7], 
        [5, 7, 3, 6, 8, 2, 9, 1, 4], 
        [1, 4, 8, 9, 5, 7, 2, 6, 3], 
        [7, 6, 5, 3, 9, 4, 8, 2, 1], 
        [9, 8, 1, 2, 7, 5, 3, 4, 6], 
        [4, 3, 2, 8, 1, 6, 7, 5, 9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

no_soln1 = [
    [1,2,3,4,5,6,7,8,0],
    [0,0,0,0,0,0,0,0,9],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

no_soln2 = [
    [1, 2, 3, 0, 0, 0, 0, 0, 0],
    [4, 5, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def solve_sudoku (grid):
    check_result = check_sudoku(grid)
    
    if check_result is None:
        # given grid is not valid
        return None
    
    if check_result == False:
        # given grid have no solution
        return False

    if check_result == True:
        if not (0 in itertools.chain(*grid)):
            # grid is valid and does not contain ZERO elements
            return grid
    
    # Такой вот примерно усредненный алгоритм:
    # 
    # search for a row with zeros
    # make a set A of all possible values for the row
    # for every zero in the row
    #   get a column
    #   make a set B of all possible values of the column
    #   get A / B (intersection) -> AB
    #   get a set C of all possible square values
    #   get AB / C -> D
    #   if D is empty - return False (no solutions)
    #   otherwise:
    #   for elt in D
    #       replace zero with elt in copy_grid
    #       recursive call solve_sudoky(copy_grid)
    #       if the result is a grid - return it
    # return False

    checkset = {1,2,3,4,5,6,7,8,9}
    squares = {}

    for y in range(9):
        row = grid[y]
        # set of missed elements
        zeros = [x for x in range(9) if row[x] == 0]
        if len(zeros) == 0:
            # the row is full, go for the new one
            continue
        
        missed_in_row = checkset.difference(row)
        # empty set of candidates for a current grid cell
        candidates = None

        for ind in zeros:
            # zero index is a X index in the grid
            x = ind
            # get a column
            column = [row[ind] for row in grid]
            missed_in_col = checkset.difference(column)
            candidates = missed_in_row
            candidates.intersection_update(missed_in_col)
            
            # get a square elements
            xs = ind//3
            ys = y//3
            coord = (xs, ys)
            square = None
            if coord not in squares:
                square = [ grid[yy][xs*3:xs*3+3] for yy in range(ys*3, ys*3+3) ]
                square = itertools.chain(*square)
                squares[coord] = square
            
            square = squares[coord]
            missed_in_square = checkset.difference(square)
            candidates.intersection_update(missed_in_square)

            if len(candidates) == 0:
                return False

            for cand in candidates:
                grid[y][x] = cand
                solution = solve_sudoku(grid)
                if solution is None or solution is False:
                    grid[y][x] = 0
                else:
                    return solution

        # if we checked all zeros 
        # and didnt find a solution 
        # we must abort cycle (to not process next rows)
        return False

    return False

def solve_with_bruteforce(grid):
    """ Bruteforce solver from course's solution """

    res = check_sudoku(grid)
    if res is None or res is False:
        return res
    
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for n in range(1,10):
                    grid[row][col] = n
                    solution = solve_with_bruteforce(grid)
                    if solution is False:
                        grid[row][col] = 0
                    else:
                        return solution
                return False
    return grid

def measure_execution_time(func, message = None, *args):
    start = time.process_time()
    result = func(*args)
    end = time.process_time()
    msg = f'Execution of {message} took {end-start} seconds\nResult is: {result}\n'
    print(msg)

def test():
        
    print(solve_sudoku(ill_formed)) # --> None
    print(solve_sudoku(invalid))    # --> False
    print(solve_sudoku(valid))      # --> Unchanged grid
    print(solve_sudoku(easy))       # --> Solved grid
    # Не запускай, подумой !
    # print(solve_sudoku(hard))       # --> Solved grid
    print(solve_sudoku(no_soln1))   # --> False
    print(solve_sudoku(no_soln2))   # --> False

def test_bruteforce_solver():

    print(solve_with_bruteforce(ill_formed))
    print(solve_with_bruteforce(invalid))
    print(solve_with_bruteforce(valid))
    print(solve_with_bruteforce(easy))

