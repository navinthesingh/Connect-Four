width = 7
height = 6
turn = 1
arr = [["|_" for j in range(width)] for i in range(height)]


def display_grid(w, h, grid):
    print("\n")
    for i in range(h):
        print(i, end=" ")
        for j in range(w):
            print(grid[i][j], end="")
        print("|")
    print(" ", end=" ")
    for index in range(w):
        print(" " + str(index), end="")


def insert_disc(h, grid, r, player):
    for i in range(h):
        if grid[h-i-1][r] == "|_":
            grid[h-i-1][r] = "|"+str(player)
            break


def check_winner(grid, w, h, player):
    win = False
    # Check Horizontal win
    for r in range(w - 3):
        for c in range(h):
            if grid[c][r] == "|"+str(player) and grid[c][r + 1] == "|"+str(player) \
                    and grid[c][r + 2] == "|"+str(player) and grid[c][r + 3] == "|"+str(player):
                win = True

    # Check vertical win
    for r in range(w):
        for c in range(h - 3):
            if grid[c][r] == "|"+str(player) and grid[c + 1][r] == "|"+str(player) \
                    and grid[c + 2][r] == "|"+str(player) and grid[c + 3][r] == "|"+str(player):
                win = True

    # Check positive diagonal
    for r in range(w):
        for c in range(h - 3):
            if grid[c][r] == "|"+str(player) and grid[c + 1][r - 1] == "|"+str(player) \
                    and grid[c + 2][r - 2] == "|"+str(player) and grid[c + 3][r - 3] == "|"+str(player):
                win = True

    # Check Negative diagonal
    for r in range(w - 3):
        for c in range(h - 3):
            if grid[c][r] == "|"+str(player) and grid[c + 1][r + 1] == "|"+str(player) \
                    and grid[c + 2][r + 2] == "|"+str(player) and grid[c + 3][r + 3] == "|"+str(player):
                win = True

    return win


running = True
# ans = False

print("+----------------+")
print("|    CONNECT 4   |")
print("+----------------+")
display_grid(width, height, arr)
print("\n")


while True:
    option = int(input("Which player starts first?(X == 1, O == 0): "))
    if option == 1:
        turn = 1
        break
    elif option == 0:
        turn = 0
        break
    else:
        print("Invalid Option!!!")

while running:

    if turn == 1:
        print("Player X turn")
        row = int(input("Enter  number to insert disc: "))

        insert_disc(height, arr, row, "X")
        display_grid(width, height, arr)
        if check_winner(arr, width, height, "X"):
            print("\nPlayer X won")
            running = False

        turn = 0
        print("\n")
    elif turn == 0:
        print("Player O turn")
        row = int(input("Enter row number to insert disc: "))

        insert_disc(height, arr, row, "O")
        display_grid(width, height, arr)
        if check_winner(arr, width, height, "O"):
            print("\nPlayer O won")
            running = False
        turn = 1
        print("\n")
