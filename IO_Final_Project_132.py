class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    #DISPLAY
    def print_board(self):
        print("\n    0   1   2")
        print("  -------------")
        for i, row in enumerate(self.board):
            print(f"{i} | " + " | ".join(row) + " |")
            print("  -------------")
        print()

    #GAME LOGIC
    def check_winner(self):
        b = self.board
        p = self.current_player

        # rows
        for row in b:
            if all(cell == p for cell in row):
                return True

        # columns
        for col in range(3):
            if all(b[row][col] == p for row in range(3)):
                return True

        # diagonals
        if all(b[i][i] == p for i in range(3)):
            return True

        if all(b[i][2 - i] == p for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    #INPUT 
    def get_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player} (row col): ").split()

                if len(move) != 2:
                    print("Enter TWO numbers: row col")
                    continue

                row, col = map(int, move)

                if row not in range(3) or col not in range(3):
                    print("Row/col must be 0–2.")
                    continue

                if self.board[row][col] != " ":
                    print("That spot is taken.")
                    continue

                return row, col

            except ValueError:
                print("Invalid input. Example: 1 2")

    #GAME LOOP
    def play(self):
        print("\n=== TIC TAC TOE ===")

        while True:
            self.print_board()

            row, col = self.get_move()
            self.board[row][col] = self.current_player

            if self.check_winner():
                self.print_board()
                print(f"\n🎉 Player {self.current_player} wins!")
                break

            if self.is_draw():
                self.print_board()
                print("\n🤝 It's a draw!")
                break

            self.current_player = "O" if self.current_player == "X" else "X"


#RUN
if __name__ == "__main__":
    game = TicTacToe()
    game.play()



