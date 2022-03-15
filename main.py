import numpy as np


class TicTacToe():
    def __init__(self):
        self.board = np.array([
            ['-']*3,
            ['-']*3,
            ['-']*3
        ])
        self.player = ''

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def fix_blank_spot(self, row, col, player):
        requested_spot = self.board[row,col]
        if requested_spot == '-':
            self.board[row,col] = player

    def is_player_win(self, player):
        win = None
        
        # Checking Rows 
        for i in range( 3 ):
            win = True
            for j in range(3):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        
        # Checking Columns
        for i in range(3):
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        
        # Checking Diagnoals
        win = True
        for i in range(3):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(3):
            if self.board[i][(3) - 1 - i] != player:
                win = False
                break
        if win:
            return win

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True


    def swap_player(self, player):
        return 'X' if player =='O' else 'O'

            
        

    def start(self):
        options = ['X', 'O']
        player_chose = input('X / O: ').upper()
        if player_chose in options:
            player = player_chose
            while True:
                
                print(f"Player {player}'s turn")
                
                self.show_board()

                row,col = list(map(int, input("Enter row and column numbers to fix the spot: ").split()))
                self.fix_blank_spot(row-1, col-1, player=player)
                
                
                if self.is_player_win(player):
                    print(f"Player {player} Wins!")
                    break
                
                if self.is_board_filled():
                    print("Match Draw!")
                    break
                    
                player = self.swap_player(player=player)
                self.show_board()
            print()
            self.show_board()

game = TicTacToe()
game.start()
