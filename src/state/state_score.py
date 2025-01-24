import game_state

# This file retreives the current board score in relation to the bot (black)
# It derives its score from the current piece values, the board position,
# and the potential threats that exist
#
# The search is not exhaustive but it gives the bot a value to rate its postion


def get_board_score(state: str):
    gameState = game_state.GameState(state)
    currentScore = 0

    # Call the three score calculators
    currentScore += piece_score(gameState.get_board_as_string())


def piece_score(pieces: str):

    piecesList = []
    for char in pieces:
        piecesList.append(char)

    runningTotal = 0

    for piece in piecesList:
        match piece:
            case "p":
                runningTotal += 1
                continue
            case "n" | "b":
                runningTotal += 3
                continue
            case "r":
                runningTotal += 5
                continue
            case "q":
                runningTotal += 9
                continue
            case _:
                continue

    return runningTotal
