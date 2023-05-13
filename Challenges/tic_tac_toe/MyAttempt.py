"""
    Task: tic tac toe Winner Checker
    Context: General Competitive Problems
    Category: Challenges

    Problem Statement: You will be given a completed board of Tic-Tac-Toe. 
    The cells will be represented by 'X' and 'O'. If there are any empty cells, 
    they will be represented by '#'. 'X' is used by Player 1 
    and 'O' is used by Player 2. Given the board, print Player 1 if player 1 wins, 
    print Player 2 if player 2 wins, and print "Draw" in case of a Tie. 
    It is guaranteed that all tic-tac-toe boards given in input are valid.

    Input:
    3x3 Tic Tac Toe board. 3 lines containing 3 characters each separated by spaces.

    X  O  X
    O  X  X
    O  O  X

"""
def TicTacToeWinnerChecker(arr) -> str:
    for i in range(3):
        if all(arr[i][j] =='X' for j in range(3)):
            return 'Player 1'
        if all(arr[i][j] == 'O' for j in range(3)):
            return 'Player 2'
        if all(arr[j][i] == 'X' for j in range(3)):
            return 'Player 1'
        if all(arr[j][i] == 'O' for j in range(3)):
            return 'Player 2'
    
    if all(arr[z][z] == 'X' for z in range(3)):
        return 'Player 1'
    if all(arr[z][2-z] == 'X' for z in range(3)):
        return 'Player 1'
    if all(arr[z][z] == 'O' for z in range(3)):
        return 'Player 2'
    if all(arr[z][2-z] == 'O' for z in range(3)):
        return 'Player 2'
    return 'Draw'

# Example usage
board_arr = [
    ['O', 'O', 'O'],
    ['#', 'X', 'O'],
    ['O', '#', 'X']
]

print(TicTacToeWinnerChecker(arr=board_arr))

"""
Output>>>
    
    Player 2
"""