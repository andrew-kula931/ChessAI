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


# This finds the raw piece score for black
def piece_score(pieces: list[str]):

    runningTotal = 0

    for piece in pieces:
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


# Pieces = grid and castling_rights = short string
def positional_score(pieces: list[str], castling_rights: str):

    totalScore = 0

    # Runs through grid and documents all relevant positions
    piece_locs = {}
    for y in range(len(pieces)):
        for x in range(len(pieces[y])):
            if pieces[y][x] not in piece_locs:
                piece_locs[pieces[y][x]] = [(x, y)]
            else:
                piece_locs[pieces[y][x]].append((x, y))

    # King safety
    kingX, kingY = piece_locs['k'][0]

    if 'k' in castling_rights or 'q' in castling_rights:
        totalScore += 1

    if kingY == 0:
        totalScore += 1
    elif kingY > 1:
        totalScore -= 1

    # Checks nearby pawns
    front_pawns = list(
        filter(lambda x: x[0] >= kingX - 1 and x[0] <= kingX + 1 and x[1] == kingY + 1, piece_locs['p']))
    side_pawns = list(
        filter(lambda x: (x[0] == kingX - 1 or x[0] == kingX + 1) and x[1] == kingY, piece_locs['p']))
    totalScore += len(front_pawns) + len(side_pawns)

    return totalScore


state = game_state.GameState(
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
positional_score(state.get_board(), 'KQkq')
