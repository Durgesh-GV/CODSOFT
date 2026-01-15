# ---------------------------------------
# TIC TAC TOE AI (MINIMAX) - IDLE SAFE
# ---------------------------------------

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---+---+---")
    print()

def check_winner(p):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -100
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"

def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("❌ Enter a number between 1 and 9.")

            elif board[move] != " ":
                print("⚠️ Position already taken!")

            else:
                board[move] = "X"
                break

        except ValueError:
            print("❌ Enter numbers only.")

# ---------------- MAIN PROGRAM ----------------

print("TIC TAC TOE - YOU (X) vs AI (O)")
print("Use the numbers below to choose your position:\n")

print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

print_board()

result = None   # store final result

while True:
    human_move()
    print_board()

    if check_winner("X"):
        result = "🎉 You win!"
        break

    if is_draw():
        result = "🤝 It's a draw!"
        break

    ai_move()
    print_board()

    if check_winner("O"):
        result = "🤖 AI wins!"
        break

    if is_draw():
        result = "🤝 It's a draw!"
        break

# -------- DISPLAY RESULT SAFELY (IDLE FIX) --------
print(result)
input("Press Enter to exit...")
