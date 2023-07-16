import re
board = [["*" for x in range(3)] for y in range(3)]
regex_pattern = r'^[0-2]$'
player = "X"



def check_winner(player,board):
    if (( board[0][0] and board[0][1] and board[0][2] ) == player) or \
       (( board[1][0] and board[1][1] and board[1][2] ) == player) or \
       (( board[2][0] and board[2][1] and board[2][2] ) == player) or \
       (( board[0][0] and board[1][1] and board[2][2] ) == player) or \
       (( board[0][2] and board[1][1] and board[2][0] ) == player):

        print("gracz wygrał:" + player)
        return True; 
    
def print_board(board):
    for x in board:
        print("\n")
        for y in x:
            print(y+ " ", end="")


def change_player(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    print("Aktualny gracz:" + player)
    return player

while 1:
    

    print_board(board)


    try:
        x_player = input("podaj koordynat x (0-2):")
        y_player = input("podaj koordynat y (0-2):")


        #Debug break
        if x_player == "Z":
            break



        if re.match(regex_pattern,x_player) and re.match(regex_pattern,y_player):
            y_player = int(y_player)
            x_player = int(x_player)


            # print(board[y_player][x_player])
            if board[y_player][x_player]  != "O" and board[y_player][x_player]  != "X":
                board[y_player][x_player] = player

                winner = check_winner(player,board)


                if winner == True:
                    break
                else:
                    player = change_player(player)
            else:
                print("pole już zajęte") 
 



    except:
        print("ma być cyfra")

    
        




# print(board)