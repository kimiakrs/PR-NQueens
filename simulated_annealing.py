#Now we want to implement Simulated Annealing (SA) algoritm to solve N-queens problem 
#It's used to find solutions for large numbers
#Annealing is the process of heating up and then cooling it very slowly (to escape from bad situations)
#we make changes randomly even bad ones.
#the algorithm jumps arounds and trying lots of things, even accepting bad moves
#Over time, temperature cools and then this algorithm will help those changes that make us to find better answers.
#We use randomness which can be useful for escaping from traps.
#we evaluate some key factors including start_temp, steps, and cooling for reaching the best answer for solving N-Queens


#Use time and tracemalloc for estimating time and memory usage
import time
import tracemalloc
#Drawing chessboard with queens
import matplotlib.pyplot as plt
#generating random numbers
import random

#To count how many pairs of queens are attackting each other in chessboard
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

#Using Simulated Annealing solution to solve N-Queens
#how many tries and steps the algorithm need before it gives up
#Adding start_temp to know how much randomness is allowed to control
#Adding cooling variable to know how quickly the temprature drops (slower cooling value or high-speed value)
def SA_solution(N, max_steps=100000000, start_temp=600.0, cooling=0.9995):
    #We start with getting random board
    board = [random.randint(0, N-1) for _ in range(N)]
    #Inital temperature
    init_temp = start_temp
    #Repeat for maximum number of steps
    for step in range(max_steps):
        #calculating pairs of attacking queens
        current_conflict = conflict_queens(board)
        if current_conflict == 0:
            #We found a valid solution
            return board, step
        #we pick one quick and try to move queen to another place to generate (a neighbor state)
        #we create row and col randomly to move our queen in that place
        row = random.randint(0, N-1)
        col = random.randint(0, N-1)

        while col == board[row]:
                col = random.randint(0, N-1)
        #copy the move and make the move
        new_board = board[:]
        #now we change the queen position to her new place
         # it means if queen place at row 1 column 2 / we will move the queen after generating random number to the new state row 3 column 0
        new_board[row] = col

        #Calculate the number of conflicts
        new_conflicts = conflict_queens(new_board)
        #conflict changes computation 
        delta = new_conflicts - current_conflict

        #Acctually it depends on a temperature we select and it has an apposite effect for choosing movements
        #we call it metropolis criterion
        #If your temperature is high, it's better to accept worse ones.
        #and when your temperature drops it would be better to accept better moves.
        #this mathematical line is for the acceptance probability for worse moves.
        #We are going to reduce the number of conflicts it means we always accept possibilities.
        if delta < 0 or random.random() < (2.71728 ** (-delta / init_temp)):
            board = new_board
        #we reduce temperature
        init_temp *= cooling
        #Prevent temprature from being zero
        if init_temp < 1e-6:
            init_temp = 1e-6

    return None, max_steps


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



def main_execution(N):
    start = time.time()
    tracemalloc.start()
    solutions, steps = SA_solution(N)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"N= {N}")
    print(f"Found solution: {'Yes' if solutions else 'No'}")
    print(f"Steps: {steps}")
    print(f"Peak Memory: {peak/1024:.2f} KB")
    print(f"Time: {end-start:.4f} s")

    if solutions:
        print("Here is our ChessBoard:")
        draw_chessboard(solutions)

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

