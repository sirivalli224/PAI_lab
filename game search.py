# Simple Tic-Tac-Toe with Minimax

board = [" "] * 9   # 9 empty positions

# Print board
def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    
    if " " not in board:
        return "Draw"
    
    return None

# Minimax function
def minimax(is_ai):
    result = check()
    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    if is_ai:  # AI turn (maximize)
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best:
                    best = score
        return best
    else:  # Human turn (minimize)
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                if score < best:
                    best = score
        return best

# Find best move for AI
def ai_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
while True:
    show()
    
    # Human move
    pos = int(input("Enter position (0-8): "))
    if board[pos] != " ":
        print("Invalid move!")
        continue
    board[pos] = "X"

    if check():
        show()
        print("Result:", check())
        break

    # AI move
    board[ai_move()] = "O"

    if check():
        show()
        print("Result:", check())
        break
