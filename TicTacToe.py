## function to show the game board
def display_board(board):
    print(" ")
    print (board[1],'|',board[2],'|',board[3])
    print ('---------')
    print (board[4],'|',board[5],'|',board[6])
    print ('---------')
    print (board[7],'|',board[8],'|',board[9])

## function to let player 1 choose a marker X or O
def choose_marker(player1_marker):
    while player1_marker not in ['X','O']:
        player1_marker = input("Player 1, Would you like to be X or O?: ").upper()
        if player1_marker not in ['X','O']:
            print("please choose X or Y")
    if player1_marker == 'X':
        return {'Player 1':'X','Player 2': 'O'}
    if player1_marker == 'O':
        return {'Player 1':'O','Player 2': 'X'}

## function to request a location to mark from player
def mark_location(board, current_player):
    location = 'wrong'
    while location not in ['1','2','3','4','5','6','7','8','9'] or board[int(location)] != '#':
        location = input(f"{current_player} ({player_markers[current_player]}) please choose a location (1-9) to mark: ")
        if location not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry, that is not a valid input")
        elif board[int(location)] != '#':
            print("Sorry, this location is already marked!")
        
    return int(location)
## function to place correct marker in selected location
def place_marker(board,location,player,player_markers):
    if player == 'Player 1':
        board[location] = player_markers['Player 1']
    elif player == 'Player 2':
        board[location] = player_markers['Player 2']

## function to check if game board has a winner in current state

def check_game(game_board, current_player, player_markers):
    no_winner = True
    if game_board[1] == game_board[2] == game_board[3] == player_markers[current_player]:
        return False
    elif game_board[4] == game_board[5] == game_board[6] == player_markers[current_player]:
        return False
    elif game_board[7] == game_board[8] == game_board[9] == player_markers[current_player]:
        return False
    elif game_board[1] == game_board[4] == game_board[7] == player_markers[current_player]:
        return False
    elif game_board[2] == game_board[5] == game_board[6] == player_markers[current_player]:
        return False
    elif game_board[3] == game_board[6] == game_board[9] == player_markers[current_player]:
        return False
    elif game_board[1] == game_board[5] == game_board[9] == player_markers[current_player]:
        return False
    elif game_board[3] == game_board[5] == game_board[7] == player_markers[current_player]:
        return False
    else:
        return True       

# function to check if there is a draw
def check_draw(in_progress,game_board):
    if in_progress == True and '#' not in game_board[1:]:
        return True
    else:
        return False
    
## running the game
in_progress = True
is_draw = False
current_player = 'Player 1'
game_board = ['#','#','#','#','#','#','#','#','#','#']
player_markers = {'Player 1':'wrong','Player 2': 'wrong'}

display_board(game_board)
player_markers = choose_marker(player_markers['Player 1'])
print(f"Great! Player 1 is {player_markers['Player 1']} and Player 2 is {player_markers['Player 2']}.")

while in_progress and not is_draw:
    current_location = mark_location(game_board, current_player)
    place_marker(game_board,current_location,current_player,player_markers)
    display_board(game_board)
    in_progress = check_game(game_board, current_player, player_markers)
    is_draw = check_draw(in_progress,game_board)
    if current_player == 'Player 1':
        current_player = 'Player 2'
    elif current_player == 'Player 2':
        current_player = 'Player 1'

if is_draw:
    print ("\nIts a draw!")
else:
    if current_player == 'Player 1':
        current_player = 'Player 2'
    elif current_player == 'Player 2':
        current_player = 'Player 1' 
    print(f"\nCongrats {current_player} ({player_markers[current_player]}), you won!")
