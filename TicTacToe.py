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
    
#function to replay game
def replay_game():
    play_again = 'wrong'
    while play_again not in ['Y','N']:
        play_again = input("Would you like to play again? Y or N: ").upper()
        if play_again not in ['Y','N']:
            print ("Please type Y or N")
    return play_again
    
## Simple introduction to the game and an explanation of the grid numbering

print("Welcome to my Tic Tac Toe game! The grid locations are numbered as follows:")
print(" ")
print ('1','|','2','|','3')
print ('---------')
print ('4','|','5','|','6')
print ('---------')
print ('7','|','8','|','9')

## The loop will check if the players want to replay at the end of each game
keep_playing = 'Y'
while keep_playing == 'Y':
    ## Initialize game variables
    in_progress = True
    is_draw = False
    current_player = 'Player 1'
    game_board = ['#','#','#','#','#','#','#','#','#','#']
    player_markers = {'Player 1':'wrong','Player 2': 'wrong'}
    
    ## First player gets to choose their marker and a dictionary is defined
    player_markers = choose_marker(player_markers['Player 1'])
    print(f"Great! Player 1 is {player_markers['Player 1']} and Player 2 is {player_markers['Player 2']}.")

    # Rounds where respective markers are placed at chosen locations
    while in_progress and not is_draw:
        current_location = mark_location(game_board, current_player)
        place_marker(game_board,current_location,current_player,player_markers)
        display_board(game_board)
        ## check and assign game status
        in_progress = check_game(game_board, current_player, player_markers)
        is_draw = check_draw(in_progress,game_board)
        
        ## Flip to other player for the following round
        if current_player == 'Player 1':
            current_player = 'Player 2'
        elif current_player == 'Player 2':
            current_player = 'Player 1'
        
    ## Depending on game status, print out a final result
    if is_draw:
        print ("\nIts a draw!")
    else:
        if current_player == 'Player 1':
            current_player = 'Player 2'
        elif current_player == 'Player 2':
            current_player = 'Player 1' 
        print(f"\nCongrats {current_player} ({player_markers[current_player]}), you won!")
    ## Ask if the players would like to play again
    keep_playing = replay_game()
    
print("Thanks for playing!")
