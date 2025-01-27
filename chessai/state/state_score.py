from .game_state import GameState


# This file retreives the current board score in relation to the bot (black)
# It derives its score from the current piece values, the board position,
# and the potential threats that exist
#
# The search is not exhaustive but it gives the bot a value to rate its postion


def get_board_score(state: str):
    gameState = GameState(state)
    currentScore = 0

    # Call the three score calculators
    currentScore += piece_score(gameState.get_board())
    currentScore += positional_score(gameState.get_board(),
                                     gameState.castleAvailability)

    return currentScore


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


def pieces_dict(pieces):
    # Documents all the pieces for easy access to individual coordinates

    piece_locs = {}

    for y in range(len(pieces)):
        for x in range(len(pieces[y])):
            if pieces[y][x] not in piece_locs:
                piece_locs[pieces[y][x]] = [(x, y)]
            else:
                piece_locs[pieces[y][x]].append((x, y))

    return piece_locs


def positional_score(pieces: list[str], castling_rights: str):

    score = 0
    piece_locs = pieces_dict(pieces)

    # King safety
    kingX, kingY = piece_locs['k'][0]

    if 'k' in castling_rights or 'q' in castling_rights:
        score += 1

    if (kingX == 3 or kingX == 4) and (kingY == 3 or kingY == 4):
        score -= 1

    # Checks pawns nearby the king
    front_pawns = list(
        filter(lambda x: kingX - 1 <= x[0] <= kingX + 1 and x[1] == kingY + 1, piece_locs['p']))
    side_pawns = list(
        filter(lambda x: (x[0] == kingX - 1 or x[0] == kingX + 1) and x[1] == kingY, piece_locs['p']))
    score += len(front_pawns) + len(side_pawns)

    # Center control
    center_corners = [pieces[3][3], pieces[3][4], pieces[4][3], pieces[4][4]]
    for corner in center_corners:
        if corner.islower():
            score += 1
        elif corner == 'p' or corner == 'q':
            score += 1

    # Moveability
    for piece in piece_locs:
        if piece.islower():
            for x, y in piece:
                available_moves(pieces, piece, (x, y))

    return score


def available_moves(pieces, type: str, position):
    def blank_check(value):
        nonlocal score

        # Returns true if it finds a blank spot and false if not
        if value == '.':
            score += .1
            return True
        return False

    score = 0
    x, y = position

    # King movement
    if type == 'k':
        for dy in range(-1, 2, 1):
            for dx in range(-1, 2, 1):
                if y + dy < 0 or x + dx < 0:
                    continue
                blank_check(pieces[y + dy][x + dx])

    # Rook movement
    if type == 'r':
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        active = [True, True, True, True]

        for i in range(1, 8):
            for index, (dx, dy) in enumerate(directions):
                if active[index]:
                    nx, ny = x + i * dx, y + i * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        active[index] = blank_check(pieces[ny][nx])

    # Knight Movement
    if type == 'n':
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dx, dy in moves:
            if (0 > x + dx > 8 or 0 > y + dy > 8):
                continue
            blank_check(pieces[y + dy][x + dx])

    # Bishop movments
    if type == 'b':
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        active = [True, True, True, True]

        for i in range(1, 8):
            for index, (dx, dy) in enumerate(directions):
                if active[index]:
                    nx, ny = x + i * dx, y + i * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        active[index] = blank_check(pieces[ny][nx])

    # Queen movements
    if type == 'q':
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                      (1, 1), (1, 0), (1, -1), (0, -1)]
        active = [True, True, True, True, True, True, True, True]

        for i in range(1, 8):
            for index, (dx, dy) in enumerate(directions):
                if active[index]:
                    nx, ny = x + i * dx, y + i * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        active[index] = blank_check(pieces[ny][nx])

    return score


def dangers(pieces):
    pass


'''

All below if for debugging and should be deleted after completion

'''


state = GameState(
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
print(get_board_score(state))
# positional_score(state.get_board(), 'KQkq')
# print(available_moves(state.get_board(), 'q', (3, 0)))

test_state = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
# get_board_score(test_state)
