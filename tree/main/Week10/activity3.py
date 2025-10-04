def main():
    line1 = [0,0,0]
    line2 = [0,0,0]
    line3 = [0,0,0]
    current_player = 1
    moves = 0
    while moves < 9:
        display_board(line1, line2, line3)
        print(f"Player {current_player}'s turn")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid input. Please enter numbers between 1 and 3.")
                continue
            if row == 0:
                line1 = place_marker(line1, col, current_player)
            elif row == 1:
                line2 = place_marker(line2, col, current_player)
            elif row == 2:
                line3 = place_marker(line3, col, current_player)
            else:
                print("Invalid row. Try again.")
                continue
            winner = check_winner(line1, line2, line3)
            if winner != 0:
                display_board(line1, line2, line3)
                print(f"Player {winner} wins!")
                return
            current_player = 2 if current_player == 1 else 1
            moves += 1
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    display_board(line1, line2, line3)
    print("It's a draw!")

def display_board(line1, line2, line3):
    print(f'{line1}\n{line2}\n{line3}')

def place_marker(line, position, marker):
    if line[position] == 0:
        line[position] = marker
    else:
        print("Position already taken!")
    return line

def check_winner(line1, line2, line3):
    # Check rows
    for line in [line1, line2, line3]:
        if line[0] == line[1] == line[2] != 0:
            return line[0]
    # Check columns
    for i in range(3):
        if line1[i] == line2[i] == line3[i] != 0:
            return line1[i]
    # Check diagonals
    if line1[0] == line2[1] == line3[2] != 0:
        return line1[0]
    if line1[2] == line2[1] == line3[0] != 0:
        return line1[2]
    return 0

if __name__ == "__main__":
    main()