board = {1 : ' ',2 : ' ',3 : ' ',
         4 : ' ',5 : ' ',6 : ' ',
         7 : ' ',8 : ' ',9 : ' ',}

def print_board(board):
    print(board[1] + '|' + board[2]+ '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5]+ '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8]+ '|' + board[9])
    print("\n")

print_board(board)

def free_space(position):
    if(board[position] == ' '):
        return True
    else:
        return False

def check_draw():
    for word in board.keys():
        if board[word] == ' ':
            return False
    return True

def check_win():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    else:
        return False

def check_win_mark(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    else:
        return False


def put_letter(letter,position):
    if free_space(position):
        board[position] = letter
        print_board(board)

        if(check_draw()):
            print("Draw")
            exit()

        if check_win():
            if letter == 'x':
                print("Bot wins")
                exit()
            else:
                print("Player wins")
                exit()
        return

    else:
        print("Can not put here")
        position = int(input("Enter new position: "))
        put_letter(letter,position)
        return

player = 'o'
bot = 'x'

def player_move():
    position = int(input("Enter the position: "))
    put_letter(player, position)
    return

def bot_move():
    best_score = -1000
    best_move = 0

    for word in board.keys():
        if(board[word] == ' '):
            board[word] = bot
            score = minimax(board,0,False)
            board[word] = ' '
            if(score > best_score):
                best_score = score
                best_move = word
    
    put_letter(bot,best_move)
    return

def minimax(board, key, maxi):
    if check_win_mark(bot):
        return 100
    elif check_win_mark(player):
        return -100
    elif check_draw():
        return 0
    
    if maxi:    #here is the maximazing part. The main part.
        best_score = -1000

        for word in board.keys():
            if(board[word] == ' '):
                board[word] = bot
                score = minimax(board,0,False)
                board[word] = ' '
                if(score > best_score):
                    best_score = score
        return best_score
    
    else:
        best_score = 900

        for word in board.keys():
            if(board[word] == ' '):
                board[word] = player
                score = minimax(board,key +1,True)
                board[word] = ' '
                if(score < best_score):
                    best_score = score
        return best_score

while not check_win():
    bot_move()
    player_move()
