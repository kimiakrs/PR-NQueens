# Now we want to implement Greedy (Hill Climbing) algorithm to solve N-queens Problem
#It tries to reduce the number of conflicts by picking the best local move with out getting stuck in local minimal
#It's not always guaranteed to find a solution, but is fast for small and medium N not large numbers.

#Adding libraries 
#for estimating, drawing and generating random numbers
import time
import tracemalloc
import matplotlib.pyplot as plt
import random

#To count how many pairs of queens are attackting each other in chessboard and are threaten by each other
def conflict_queens(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            #Queens are in the same column or diagonal
            #It means we compare the queen at row 'i' with every queen in a lower row 'j'
            #we check that are they in the same columns or not
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

#Greedy Search (Hill Climbing) Algorithm

def greedys_hill(N, max_restarts=20, p_sideways=0.4):
    for restart in range(max_restarts):
        #Placing each Queens randomly in any rows
        #We generate board randomly
        board = [random.randint(0, N-1) for _ in range(N)]
        steps = 0

        while True: 
            #we get the current-conflict (counting threatening locations)
            current_conflicts = conflict_queens(board)
            #If there are no conflicts, return the solution
            if current_conflicts == 0:
                print(f"This solution solved in {steps} steps.")
                print(f"Solved after {restart+1} restarts.")
                return board
            #Now we go to move each queen to every other row in its column
            best_move = None
            min_conflicts = current_conflicts
            #we add the state of queen as an original row and then we check our conflict again
            for col in range(N):
                original_row = board[col]
                #Now we check every row of that column
                for row in range(N):
                    if row == original_row:
                        continue
                    board[col] = row
                    check_conflict = conflict_queens(board)
                    #Save the best move ==> we will change our board to check_conflict if it has a few conflicts than other.
                    #We added p_sideways in our experiments to show how effectively we can inject no conflicts.
                    if check_conflict < min_conflicts or (check_conflict == min_conflicts and random.random() < p_sideways):
                        min_conflicts = check_conflict
                        #we insert column and row in best_move variable
                        best_move = (col, row)
                    board[col] = original_row
            #After searching all column, we can find the best move for the queen
            if best_move is None:
                break
            col , row = best_move
            board[col] = row
            steps += 1 
    print("No solution found after multiple restarts.")
    return None


#we want graphical output:
def draw_chessboard(board):
    N = len(board)
    # we use figure and axis where we draw square and queens
    #actually axis is contained inside the figure.
    #fig: In chess board will be my whole chessboard image
    #axis : The area you draw
    fig, ax = plt.subplots(figsize=(min(10, N/5), min(10, N/5)))
    # Draw squares
    for row in range(N):
        for col in range(N):
            color = 'white' if (row + col) % 2 == 0 else 'grey'
            #we draw recentagle in row = 0 and it will be started with white
            ax.add_patch(plt.Rectangle((col, N - row - 1), 1, 1, facecolor=color))
    # Draw Queens
            #for drawing fixed queens in our chessboard, we set minimum size and maximum size of our N
            font_size = max(200 // N, 7)
    for row, col in enumerate(board):
        # we flip our chessboard to change the location of row = 0 at the top
        ax.text(col + 0.5, N - row - 1 + 0.5, u"\u265B", fontsize=font_size, ha='center', va='center', color='blue')
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
    #show chessboard
    plt.show()

    
    #We add our metrics to be evaluated
def main_execution(N):
    start = time.time()
    tracemalloc.start()
    solution = greedys_hill(N, max_restarts=20, p_sideways=0.4)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"N= {N}")
    print(f"Found solution: {'Yes' if solution else 'No'}")
    print(f"Peak Memory: {peak/1024:.2f} KB")
    print(f"Time: {end-start:.4f} s")

    if solution:
        print("Chessboard:")
        draw_chessboard(solution)
    else:
        print("No solution found.")

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
