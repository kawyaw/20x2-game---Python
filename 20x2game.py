import random
import datetime
from prettytable import PrettyTable

#creating a atable
Table = PrettyTable(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])
Table.add_row(['']*20)
Table.add_row(['']*20)

# Define the grid size
GRID_WIDTH = 20
GRID_HEIGHT = 2

# Initialize the grid
grid = [[' '] * GRID_WIDTH for i in range(GRID_HEIGHT)]

# Define the black holes
BLACK_HOLES = [7, 14]

# Define the players' positions
player_pos = 0
computer_pos = 0

# Define the game state
game_over = False
winner = None

# Define the total black hole hits
total_black_hole_hits = 0

# Black hole hits
player_black_hole_hits = 0
computer_black_hole_hits = 0

# Define the total number of moves
human_total_moves = 0
computer_total_moves = 0

# Define the dice roll function
def roll_dice():
    return random.randint(1, 6)

# Define the move function
def move_player(player, steps):
    global BLACK_HOLES,computer_black_hole_hits,player_black_hole_hits, GRID_WIDTH
    
    # Move the player
    player += steps
    
    # Check for black holes
    if player in BLACK_HOLES:
       if player == BLACK_HOLES:
          player_black_hole_hits += 1
       else:
           computer_black_hole_hits += 1
       player = 0
        
    # Check for victory
    if player >= GRID_WIDTH:
       player = GRID_WIDTH
       return True, player
    
    return False, player

# Wait for 6 to start the game
while player_pos and computer_pos <20:
    dice_roll = roll_dice()
    if dice_roll == 6:
       print("Game started! Rolling the dice...")
       break
    else:
       print("Rolling the dice... You need a 6 to start the game!")

   
# Main game loop
while not game_over:
     # Roll the dice
    dice_roll = roll_dice()
    human_total_moves += dice_roll //2
    print("Your dice value: ",dice_roll)
       
   
     # Move the player
    if player_pos == 0 and dice_roll != 6:
       print("You need a 6 to start the game!")
    elif player_pos == 0 and dice_roll == 6:
       print("You started the game! Rolling the dice...")
       player_pos = 1
    elif player_pos == 7 or player_pos == 14:
       print("Tou hit the black hole,move to start..",BLACK_HOLES)
       player_pos = 0
       
       
    victory, player_pos = move_player(player_pos, dice_roll // 2)
    if victory:
       winner = 'human'
       game_over = True
       break
        
    # Move the computer
    #  Computer Roll dice
    computer_dice_roll = roll_dice()
    computer_total_moves += computer_dice_roll //2
    print("computer dice value: ",computer_dice_roll)
    if computer_pos == 0 and computer_dice_roll != 6:
        print("need 6 to start the game..")
    elif computer_pos == 0 and computer_dice_roll == 6:
        print("Computer started the game")
        computer_pos = 1
    elif computer_pos ==7 or computer_pos == 14:
        print("computer hit the black hole, move to start..",BLACK_HOLES)
        computer_pos = 0
    
    victory, computer_pos = move_player(computer_pos, computer_dice_roll // 2)
    if victory:
        winner = 'computer'
        game_over = True
        break
    
    # Check for game over
    if player_pos == GRID_WIDTH and computer_pos == GRID_WIDTH:
        winner = 'tie'
        game_over = True
        break

    # Check for black hole hits
    if player_pos in BLACK_HOLES:
        print("You hit the black hole..")
        player_pos = 0
        player_black_hole_hits += 1

    if computer_pos in BLACK_HOLES:
        print("Computer hit the black hole..")
        computer_pos = 0
        computer_black_hole_hits += 1
        
    # Print the grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if row == 0 and col == computer_pos:
                grid[row][col] = 'X'
            elif row == 1 and col == player_pos:
                grid[row][col] = 'X'
            elif col in BLACK_HOLES and (row == 0 or row == 1):
                grid[row][col] = 'O'
            else:
                grid[row][col] = ' '
    
    table = PrettyTable()
    table.field_names = list(range(1, GRID_WIDTH+1))
    for row in grid:
        table.add_row(row)
    print(table)
    
    # Wait for user input
    input("Press Enter to roll the dice...")
   
    
# Print the winner and total moves
if winner == 'human':
    print("Congratulations, you won!")
elif winner == 'computer':
    print("Sorry, the computer won.")
else:
    print("It's a tie!")
print("Human total moves:", human_total_moves)
print(" player black hole hits:",player_black_hole_hits)
print("Computer total moves:",computer_total_moves)
print("Computer black hole hits: ",computer_black_hole_hits)

#Get the current date and time
now = datetime.datetime.now()

# Create the filename for the text file
filename = "{}_{}_{}_{}_{}.txt".format(now.year, now.month, now.day, now.hour, now.minute)

# Open the file in write mode
with open(filename, "w") as f:
    # Write the human player's details
    f.write("Human\n")
    f.write("Total moves: {}\n".format(human_total_moves))
    f.write("Black hole hits: {}\n".format(player_black_hole_hits))
    if winner == "human":
        f.write("Won the game\n")
    else:
        f.write("Lost the game\n")

    # Write the computer player's details
    f.write("\nComputer\n")
    f.write("Total moves: {}\n".format(computer_total_moves))
    f.write("Black hole hits: {}\n".format(computer_black_hole_hits))
    if winner == "computer":
        f.write("Won the game\n")
    else:
        f.write("Lost the game\n")






