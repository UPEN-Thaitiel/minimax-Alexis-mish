BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        # Challenge 1: Initialize the board as a dictionary with keys 1-9 all set to ' '
        # Set player symbol to 'O' and computer symbol to 'X'
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        # Challenge 11: Create the main game loop
        # - Computer starts first
        # - Alternate between computer and player moves
        # - After each move, check if the game has ended (win or draw)
        # - If game ended, exit the loop and print result
        
        self.print_board()
        while True:
            self.move_computer()
            self.print_board()
            if self.check_game_state():
                break
            self.move_player()
            self.print_board()
            if self.check_game_state():
                break

    def print_board(self):
        # Challenge 2: Print the board in 3 rows and 3 columns
        # For example:
        # X | O |  
        # --+---+--
        #   | X | O
        # --+---+--
        # O |   | X
        print(self.board[1] + ' |' + self.board[2] + '  |' + self.board[3] ) 
        print('--+---+--')
        print(self.board[4] + ' |' + self.board[5] + '  |' + self.board[6] )
        print('--+---+--')
        print(self.board[7] + ' |' + self.board[8] + '  |' + self.board[9] )
        print("\n")


    def is_cell_free(self, position):
        # Challenge 3: Return True if the cell at 'position' is empty (' ')
        # Otherwise, return False
        if self.board[position] == ' ':
            return True
        return False

    def update_player_position(self, player, position):
        # Challenge 4: If the cell at 'position' is free, place 'player' symbol there
        # If the cell is occupied, print an error and ask the player to input again
        # After updating the board, check if the game ended (win or draw)
        if self.is_cell_free(position):
            self.board[position] = player
        else:
            print("Error: cannot insert here")
            self.move_player()        

    def is_winning(self, player):
        # Challenge 5: Check if 'player' has 3 in a row horizontally, vertically, or diagonally
        # Return True if winning condition met, False otherwise
        b = self.board
    # Todas las combinaciones ganadoras posibles
        winning_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),     # filas
            (1, 4, 7), (2, 5, 8), (3, 6, 9),     # columnas
            (1, 5, 9), (3, 5, 7)                 # diagonales
        ]
        for a, b_, c in winning_combinations:
            if b[a] == b[b_] == b[c] == player:
                return True
        return False

    def is_draw(self):
        # Challenge 6: Return True if no empty cells remain on the board (all positions filled)
        # and no player has won
        return all(self.board[pos] != ' ' for pos in self.board) and \
           not self.is_winning(self.player) and not self.is_winning(self.computer)

    def check_game_state(self):
        # Challenge 7: Print the board and check if the game ended
        # If player or computer won, print the winner and exit
        # If draw, print 'Draw!' and exit
        if self.is_winning(self.computer):
            print("Computer wins!")
            return True
        elif self.is_winning(self.player):
            print("You win!")
            return True
        elif self.is_draw():
            print("Draw!")
            return True
        return False

    def move_player(self):
        # Challenge 8: Ask the human player to enter a position (1-9)
        # Validate input is an integer within range and the cell is free
        # Update the board with player's move
        while True:
            try:
                position = int(input("Enter your move (1-9): "))
                if position in range(1, 10) and self.is_cell_free(position):
                    self.update_player_position(self.player, position)
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

    def move_computer(self):
        # Challenge 9: Iterate over all free cells on the board
        # For each cell, simulate placing computer's symbol and calculate minimax score
        # Choose the cell with the highest minimax score and place the computer's symbol there
        # After the move, check if the game ended
        best_score = float('-inf')
        best_move = None
        for pos in range(1, 10):
            if self.is_cell_free(pos):
                self.board[pos] = self.computer
                score = self.minimax(0, False)
                self.board[pos] = ' '
                if score > best_score:
                    best_score = score
                    best_move = pos
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, is_maximizer):
        # Challenge 10: Implement recursive minimax algorithm:
        # - If computer wins, return positive score (REWARD - depth)
        # - If player wins, return negative score (-REWARD + depth)
        # - If draw, return 0
        # - If maximizing (computer's turn), try to maximize score over all possible moves
        # - If minimizing (player's turn), try to minimize score over all possible moves
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0

        if is_maximizer:
            best_score = float('-inf')
            for pos in range(1, 10):
                if self.is_cell_free(pos):
                    self.board[pos] = self.computer
                    score = self.minimax(depth + 1, False)
                    self.board[pos] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for pos in range(1, 10):
                if self.is_cell_free(pos):
                    self.board[pos] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[pos] = ' '
                    best_score = min(best_score, score)
            return best_score


if __name__ == '__main__':
    # Challenge 1: Initialize empty board dictionary with keys 1 to 9 set to ' '
    board = {pos: ' ' for pos in range(1, 10)}

    game = TicTacToe(board)
    # Challenge 11: Start the game loop
    game.run()
