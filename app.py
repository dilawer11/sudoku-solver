import time
class SudokuSolver:
    
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 7],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 6, 0, 7, 9]
    ]
    solvedBoard = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    stack = []
    def rollback(self):
        if not len(self.stack):
            print('Unsolvable')
            return 9, 9
        row = self.stack[-1][0]
        col = self.stack[-1][1]
        currentValue = self.board[row][col]
        self.board[row][col] = 0
        self.stack.pop()
        for i in range(currentValue + 1, 10):
            if self.insertValid(row, col, i):
                self.board[row][col] = i
                self.stack.append((row, col))
                return row, col
        return self.rollback()
    def insertValid(self,row, col, value):
    # Assuming board is valid before value was entered
        # Check no duplicate in row
        for r in range(0, 9):
            if self.board[r][col] == value:
                return False
        #Check no duplicate in col
        for c in range(0, 9):
            if self.board[row][c] == value:
                return False
        #Check 3x3 grid which the row, col belong to
        for r in range(row - (row % 3), (row + (3 - (row % 3)))):
            for c in range(col - (col % 3), (col + (3 - (col % 3)))):
                if self.board[r][c] == value:
                    return False
        return True  
    def displayBoard(self):
        #time.sleep(2)
        for r in range(0, 9):
            if not r % 3:
                print('---------------------')
            for c in range(0, 9):
                if not c % 3:
                    print('|', end = '') 
                if c == 8:
                    print(self.board[r][c], end='')
                else:
                    print(self.board[r][c], end=' ')
            print('|')
        print('---------------------')
    def solve(self):
        r = 0
        while r < 9:
            c = 0
            while c < 9:
                if not self.board[r][c]:
                    inserted = False
                    for i in range(1, 10):
                        if self.insertValid(r ,c, i) and not inserted:
                            self.board[r][c] = i
                            self.stack.append((r,c))
                            inserted = True
                            break
                    if not inserted:
                        r, c = self.rollback()
                    else:
                        c += 1
                else:
                    c += 1
            # self.displayBoard()
            r += 1
        print('Done Solving')
        self.displayBoard()
def main():
    print("Welcome To Sudoku")
    ss = SudokuSolver()
    ss.displayBoard() 
    startTime = time.time()
    ss.solve()
    print("Time Taken =", time.time() - startTime)
if __name__ == "__main__":
    main()