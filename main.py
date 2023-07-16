import re
import sys

class Game:
    #init regex for inputs and starting player and fills the array with "*"
    def __init__(self):     
        self.board = [["*" for x in range(3)] for y in range(3)]
        self.regex_pattern = r'^[1-3]$'
        self.player = "X"
        self.play()

    #print board 
    def print_board(self):
        print("------------", end=" ")
        for x in self.board:
            print("\n|", end=" ")
            for y in x:
                print(y+ " | ", end="")
        print("\n------------\n", end="")
        
    #change player X - O
    def change_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
    
    #check winning contidion and ends the game if player won
    def check_winner(self):
        if (
            (self.board[0][0] == self.player and self.board[0][1] == self.player and self.board[0][2] == self.player) or
            (self.board[1][0] == self.player and self.board[1][1] == self.player and self.board[1][2] == self.player) or
            (self.board[2][0] == self.player and self.board[2][1] == self.player and self.board[2][2] == self.player) or
            (self.board[0][0] == self.player and self.board[1][1] == self.player and self.board[2][2] == self.player) or
            (self.board[0][2] == self.player and self.board[1][1] == self.player and self.board[2][0] == self.player) or
            (self.board[0][0] == self.player and self.board[1][0] == self.player and self.board[2][0] == self.player) or
            (self.board[0][1] == self.player and self.board[1][1] == self.player and self.board[2][1] == self.player) or
            (self.board[0][2] == self.player and self.board[1][2] == self.player and self.board[2][2] == self.player)
        ):

            print("Player won:" + self.player)
            self.print_board()
            sys.exit("")
        else:
            self.change_player()

    #main method where the game goes on
    def play(self):
   
        
        while 1:
            print("\nActual player:" + self.player)
            self.print_board()

            try:
                #input coords of selected field
                x_player = input("Input coordinate x (1-3): ")
                y_player = input("Input coordinate y (1-3): ")


                #Debug break - input Z to leave game
                if 0 == 1:
                    if x_player == "Z" or y_player == "Z" :
                        sys.exit("Exiting the code with sys.exit()!")

                #check regex of coords
                if re.match(self.regex_pattern,x_player) and re.match(self.regex_pattern,y_player):
                    y_player = int(y_player) - 1
                    x_player = int(x_player) - 1

                    #conditions that check if field is empty
                    if self.board[y_player][x_player]  != "O" and self.board[y_player][x_player]  != "X":
                        self.board[y_player][x_player] = self.player
                        self.check_winner()
                    else:
                        print("!!! Not empty coordinates !!!") 
                else:
                    print("!!! must be a number in 1-3 range !!!")

            except:
                sys.exit("End of the game")

start_game = Game()