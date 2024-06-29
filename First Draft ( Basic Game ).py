def display_game(positions):
    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(positions)

def is_valid_move(positions, selected_position, pos2):
    if positions[selected_position] == 'G' and pos2 < 7 and positions[pos2] == '-':
        return True
    if positions[selected_position] == 'B' and pos2 >= 0 and positions[pos2] == '-':
        return True
    return False

def check_winning_condition(positions):
    if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
        print("You Win!")
        return True
    return False

positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']
display_game(positions)

while True:
    selected_position = input("Enter the position of the frog you want to move (0-6) or 'q' to quit: ")
    if selected_position == 'q':
        break

    try:
        selected_position = int(selected_position)
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 6.")
        continue

    if selected_position < 0 or selected_position > 6:
        print("Invalid move. Position must be between 0 and 6.")
        continue

    if positions[selected_position] == '-':
        print("Invalid move. You cannot select an empty space.")
        continue

    pos2 = None
    if positions[selected_position] == 'G':
        if selected_position + 1 < 7 and positions[selected_position + 1] == '-':
            pos2 = selected_position + 1
        elif selected_position + 2 < 7 and positions[selected_position + 2] == '-' and positions[selected_position + 1] == 'B':
            pos2 = selected_position + 2
    elif positions[selected_position] == 'B':
        if selected_position - 1 >= 0 and positions[selected_position - 1] == '-':
            pos2 = selected_position - 1
        elif selected_position - 2 >= 0 and positions[selected_position - 2] == '-' and positions[selected_position - 1] == 'G':
            pos2 = selected_position - 2

    if pos2 is None or not is_valid_move(positions, selected_position, pos2):
        print("Invalid move.")
        continue

    positions[selected_position], positions[pos2] = positions[pos2], positions[selected_position]
    display_game(positions)

    if check_winning_condition(positions):
        break

print("Game Over.")

