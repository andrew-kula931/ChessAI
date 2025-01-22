# This file sets the rules for the game state which will be used
# throughout the algorithm process

class GameState:
    def __init__(self, gameState: str):
        self.gameState = gameState

        # The incoming game state will default to FEN notation

        # Example "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
        # Lowercase -> black pieces  UpperCase -> white pieces
        # b / w indicates white or black move
        # KQkq indicates b/w castling availability (Kingside or Queenside)
        # e3 indicates the move (In this case it indicates the en passant location)
        # 0 and 1 are for halfmove and fullmove clocks

        gameStateList = gameState.split(" ")

        self.board = gameStateList[0]
        self.currentTurn = gameStateList[1]
        self.castleAvailability = gameStateList[2]
        self.move = gameStateList[3]
        self.halfmoveClock = gameStateList[4]
        self.fullmoveNumber = gameStateList[5]

    def get_board(self):
        board = [[] for _ in range(8)]

        board_rows = self.board.split("/")

        # Copious nesting is required to create a board list from the string provided
        for i in range(8):
            for char in board_rows[i]:
                if char.isdigit():
                    for j in range(int(char)):
                        board[i].append(".")
                else:
                    board[i].append(char)

        return board
