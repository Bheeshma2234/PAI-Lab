solutions=0
def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1:
            return False
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=row-1,col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    return True
def print_board(board,n):
    global solutions
    print(f"\nSolution {solutions}:")
    for row in board:
        for cell in row:
            if cell==1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
def solve_nqueens(board,row,n):
    global solutions
    if row==n:
        solutions+=1
        print_board(board,n)
        return
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            solve_nqueens(board,row+1,n)
            board[row][col]=0
n=int(input("Enter number of queens: "))
board=[[0 for _ in range(n)] for _ in range(n)]
solve_nqueens(board, 0, n)
print("\nTotal Solutions =",solutions)
