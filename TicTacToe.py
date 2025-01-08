in_progress = True
current_player = 'Player 1'
game_board = ['#','#','#','#','#','#','#','#','#','#']
player_markers = {'Player 1':'wrong','Player 2': 'wrong'}

def display_board(board):
    print(" ")
    print (board[1],'|',board[2],'|',board[3])
    print ('---------')
    print (board[4],'|',board[5],'|',board[6])
    print ('---------')
    print (board[7],'|',board[8],'|',board[9])

def choose_marker(player1_marker):
    while player1_marker not in ['X','O']:
        player1_marker = input("Player 1, Would you like to be X or O?").upper()
        if player1_marker not in ['X','O']:
            print("please choose X or Y")
    if player1_marker == 'X':
        return {'Player 1':'X','Player 2': 'O'}
    if player1_marker == 'O':
        return {'Player 1':'O','Player 2': 'X'}

def mark_location(board, current_player):
    location = 'wrong'
    while location not in ['1','2','3','4','5','6','7','8','9'] or board[int(location)] != '#':
        location = input(f"{current_player} please choose a location (1-9) to mark")
        if location not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry, that is not a valid input")
        elif board[int(location)] != '#':
            print("Sorry, this location is already marked!")
        
    return int(location)

def place_marker(board,location,player,player_markers):
    if player == 'Player 1':
        board[location] = player_markers['Player 1']
    elif player == 'Player 2':
        board[location] = player_markers['Player 2']

def check_game():
    no_winner = True
    if set([game_board[1],game_board[2],game_board[3]]) == {'X'} or set([game_board[1],game_board[2],game_board[3]]) == {'O'}:
        return False
    elif set([game_board[4],game_board[5],game_board[6]]) == {'X'} or set([game_board[4],game_board[5],game_board[6]]) == {'O'}:
        return False
    elif set([game_board[7],game_board[8],game_board[9]]) == {'X'} or set([game_board[7],game_board[8],game_board[9]]) == {'O'}:
        return False
    elif set([game_board[1],game_board[4],game_board[7]]) == {'X'} or set([game_board[1],game_board[4],game_board[7]]) == {'O'}:
        return False
    elif set([game_board[2],game_board[5],game_board[8]]) == {'X'} or set([game_board[2],game_board[5],game_board[8]]) == {'O'}:
        return False
    elif set([game_board[3],game_board[6],game_board[9]]) == {'X'} or set([game_board[3],game_board[6],game_board[9]]) == {'O'}:
        return False
    elif set([game_board[1],game_board[5],game_board[9]]) == {'X'} or set([game_board[1],game_board[5],game_board[9]]) == {'O'}:
        return False
    elif set([game_board[3],game_board[5],game_board[7]]) == {'X'} or set([game_board[3],game_board[5],game_board[7]]) == {'O'}:
        return False
    else:
        return True 
    


display_board(game_board)
player_markers = choose_marker(player_markers['Player 1'])
print(f"Great! Player 1 is {player_markers['Player 1']} and Player 2 is {player_markers['Player 2']}.")

while in_progress:
    current_location = mark_location(game_board, current_player)
    place_marker(game_board,current_location,current_player,player_markers)
    display_board(game_board)
    in_progress = check_game()
    if current_player == 'Player 1':
        current_player = 'Player 2'
    elif current_player == 'Player 2':
        current_player = 'Player 1'

if current_player == 'Player 1':
    current_player = 'Player 2'
elif current_player == 'Player 2':
    current_player = 'Player 1' 
print(f"\nCongrats {current_player} ({player_markers[current_player]}), you won!")