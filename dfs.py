#Now we want to implement Exhaustive Search(DFS) algoritm to solve N-queens problem 
#It is comman to call it Back tracking which can help queens to have a returned movement to their previous positions(move recursively)

#Use time and tracemalloc for estimating time and memory usage
import time
import tracemalloc
#Drawing chessboard with queens
import matplotlib.pyplot as plt



#Make assume that we have chess-board NxN
#queens can be placed at position without being attacked by other queens? 
#we have to check that queens should not be threatened by each other from 3 positions (horizontal, diagonal, and vertical)
#We do not need any conflict with previous queens
def threaten_position_check(board, row, col):
    for i in range(row):
        #the column index of the queen in row i 
        #check if another queens are in same column or on a diagonal
        #same column
        if board[i] == col:
            return False
        #check diagonal position
        #same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


#first we will check that is our row (i) empty or not
#we need one list to store our solutions
def dfs_solution(N, row=0, board=None, solutions=None):
    if board is None:
        #initial call for our board is [-1,-1,-1,-1, ...]
        board = [-1]*N #unassigned row is -1
    if solutions is None:
        solutions = []
    if row == N:
        solutions.append(board[:]) #copy board to solutions list
        return

    #Check every column in the current row for queens
    for col in range(N):
        #Here we check  that my queen in this position is safe or not.
        if threaten_position_check(board, row, col):
            #if she is safe so we put it into this state
            board[row] = col #add queen in this row and column
            dfs_solution(N, row+1, board, solutions) #we add 1 for checking 
            board[row] = -1 #Remove Queen for trying next step
    return solutions


#we want graphical output:
def draw_chessboard(board):
    N = len(board)
    # we use figure and axis where we draw square and queens
    #actually axis is contained inside the figure.
    #fig: In chess board will be my whole chessboard image
    #axis : The area you draw
    fig, ax = plt.subplots()
    # Draw squares
    for row in range(N):
        for col in range(N):
            color = 'white' if (row + col) % 2 == 0 else 'grey'
            #we draw recentagle in row = 0 and it will be started with white
            ax.add_patch(plt.Rectangle((col, N - row - 1), 1, 1, facecolor=color))
    # Draw Queens
    for row, col in enumerate(board):
        # we flip our chessboard to change the location of row = 0 at the top
        ax.text(col + 0.5, N - row - 1 + 0.5, u"\u265B", fontsize=30, ha='center', va='center', color='blue')
    #we set this to see row and column in range of (0, N)
    #from the left edge to the right edge, so we can see all columns 
    #Now all columns are visible
    ax.set_xlim(0, N)
    #from the bottom to the top, so we can see all rows
    #all rows are visible
    ax.set_ylim(0, N)
    #here we remove all marks or numbers on the side of the plot
    ax.set_xticks([])
    ax.set_yticks([])
    #making sure the width and height of each square are equal
    ax.set_aspect('equal')
    #to show chessboard
    plt.show()

#we want to estimate our time, memory usage , and find out that are we able to find solutions for our N queens or not
# we add performance metrics (tracemalloc, time)
def main_execution(N):
    start = time.time()
    tracemalloc.start()
    find_solution = dfs_solution(N)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"N= {N}")
    print(f"Number of solutions: {len(find_solution)}")
    print(f"Peak Memory: {peak/1024/1024:.2f} MB")
    print(f"Time: {end-start:.4f} s")

    if find_solution:
        print("Chessboard:")
        draw_chessboard(find_solution[0])

    else:
        print("No solution found.")

def draw_empty_chessboard(N):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    for row in range(N):
        for col in range(N):
            color = 'white' if (row + col) % 2 == 0 else 'grey'
            ax.add_patch(plt.Rectangle((col, N - row - 1), 1, 1, facecolor=color))
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.show()


if __name__ == "__main__":
    allowed_numbers = [10, 30, 50, 100, 200]
    print(f"Please enter the number of queens (N) to solve. Choose one of: {allowed_numbers}")
    while True:
        try:
            N = int(input("Enter the number of queens(N): "))
            if N in allowed_numbers:
                break
            else:
                print("Invalid input. Please select one of:", allowed_numbers)
        except Exception as e:
            print("Invalid input. Please enter a number.")
    main_execution(N)
    




















