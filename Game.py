import pygame
import sys

# It initialize the pygame library
pygame.init()

# Using this to set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Defining color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Loading frog images from files
green_frog_image = pygame.image.load("green_frog.png")  # Sir make sure to download the images too
brown_frog_image = pygame.image.load("brown_frog.png")

# Resizing the images to fit within the grid cells
green_frog_image = pygame.transform.scale(green_frog_image, (100, 100))
brown_frog_image = pygame.transform.scale(brown_frog_image, (100, 100))

# Creating the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frog Leap Game")

# Initial positions of the frogs on the game board
positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']

# It define the font for messages
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Function to display the game state on the screen
def display_game(message=""):
    screen.fill(WHITE)  # Clear the screen
    for i in range(7):  # Loop through each position on the board
        x = 100 * i + 50  # Calculate x coordinate for the frog
        y = 100  # Set y coordinate for the frog
        if positions[i] == 'G':  # If there's a green frog at this position
            screen.blit(green_frog_image, (x, y))
        elif positions[i] == 'B':  # If there's a brown frog at this position
            screen.blit(brown_frog_image, (x, y))
        pygame.draw.rect(screen, BLACK, (x, y, 100, 100), 1)  # Draw a border around the grid cell

    if message:  # If there's a message to display
        msg = font.render(message, True, RED if "Invalid" in message or "Try Again" in message else GREEN)
        screen.blit(msg, (150, 250))  # Display the message on the screen

    # It draws the reset button
    reset_button = pygame.Rect(350, 300, 100, 50)
    pygame.draw.rect(screen, BLUE, reset_button)
    reset_text = small_font.render("RESET", True, WHITE)
    screen.blit(reset_text, (reset_button.x + 10, reset_button.y + 10))

    pygame.display.flip()  # Update the display

# Function to check if a move is valid
def is_valid_move(selected_position, pos2):
    if positions[selected_position] == 'G' and pos2 < 7 and positions[pos2] == '-':
        return True
    if positions[selected_position] == 'B' and pos2 >= 0 and positions[pos2] == '-':
        return True
    return False

# Function to check if the game is won
def check_winning_condition():
    if positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']:
        return True
    return False

# Function to check if there are any valid moves left
def has_valid_moves():
    for i in range(7):
        if positions[i] == 'G':  # Check moves for green frogs
            if (i + 1 < 7 and positions[i + 1] == '-') or (i + 2 < 7 and positions[i + 2] == '-' and positions[i + 1] == 'B'):
                return True
        elif positions[i] == 'B':  # Check moves for brown frogs
            if (i - 1 >= 0 and positions[i - 1] == '-') or (i - 2 >= 0 and positions[i - 2] == '-' and positions[i - 1] == 'G'):
                return True
    return False

# Function to reset the game to its initial state
def reset_game():
    global positions
    positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']
    display_game()

# Main game loop
def game_loop():
    display_game()  # Initial display

    while True:  # Main game loop
        for event in pygame.event.get():  # Check for events
            if event.type == pygame.QUIT:  # If the user wants to quit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks the mouse
                x, y = event.pos  # Get the position of the click
                if 350 <= x <= 450 and 300 <= y <= 350:  # Check if the reset button is clicked
                    reset_game()  # Reset the game
                    continue

                pos = (x - 50) // 100  # Calculate the position in the grid
                if pos < 0 or pos > 6:  # Check if the click is within the grid
                    continue
                if positions[pos] in ['G', 'B']:  # Check if a frog is selected
                    selected_position = pos
                    pos2 = None
                    if positions[selected_position] == 'G':  # Check possible moves for green frog
                        if selected_position + 1 < 7 and positions[selected_position + 1] == '-':
                            pos2 = selected_position + 1
                        elif selected_position + 2 < 7 and positions[selected_position + 2] == '-' and positions[selected_position + 1] == 'B':
                            pos2 = selected_position + 2
                    elif positions[selected_position] == 'B':  # Check possible moves for brown frog
                        if selected_position - 1 >= 0 and positions[selected_position - 1] == '-':
                            pos2 = selected_position - 1
                        elif selected_position - 2 >= 0 and positions[selected_position - 2] == '-' and positions[selected_position - 1] == 'G':
                            pos2 = selected_position - 2

                    if pos2 is not None and is_valid_move(selected_position, pos2):  # Make the move if valid
                        positions[selected_position], positions[pos2] = positions[pos2], positions[selected_position]
                        if check_winning_condition():  # Check if the game is won
                            display_game("You Win!")
                        elif not has_valid_moves():  # Check if there are no valid moves left
                            display_game("Try Again!")
                        else:
                            display_game()  # Update the display
                    else:
                        display_game("Invalid Move!")  # Display invalid move message

# Run the game
game_loop()


# Sir I have tried my best to give comments for the easy understanding of code
# Please make sure to download images before Executing the code