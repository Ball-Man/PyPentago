import model.turn_controller as turn_controller
import model.pentago as pentago
import enum
import re

from os import system, path, name as sysname
from termcolor import colored

# Constants
TITLE_FILENAME = 'files/title.txt'

CMD = '>> '
INPUT_ERROR = 'Please follow the syntax as shown in the line above'
QUIT_CMD = 'quit'
NEW_GAME = 'new_game'



hor_test = '─/┼/╬/═/║'

PAWN = 'O'
VERT_SEP = '║'
HOR_SEP = '═'
SPACE = ' '
MIDDLE_LINE = '║═══════╬═══════║'

COLORS = { pentago.WHITE: 'white', pentago.BLACK: 'red' }

ROW_IDS = ['1', '2', '3', '4', '5', '6']
COL_IDS = ['a', 'b', 'c', 'd', 'e', 'f']

ROT_DICT = { 'cw': pentago.CLOCKWISE, 'cc': pentago.COUNTCLOCKWISE }

class GameState(enum.Enum):
    PLACE = 0
    ROTATE = 1
    QUIT = 2
    OVER = 3

WINNER_TOKEN = '%winner%'
YES = 'y'
NO = 'n'
STATUS_DICT = {
    GameState.PLACE: 'Where do you want to place your pawn? (e.g. b5)',
    GameState.ROTATE: 'What sector do you want to rotate? (e.g. 2cw)',
    GameState.OVER: f'The game is over, the winner is: {WINNER_TOKEN}\nRestart? (y/[n])'
}

TURN_STRING = "It's the turn of "

WINNER_DICT = {
    pentago.WHITE: 'the white pawn',
    pentago.BLACK: 'the black pawn',
    pentago.DRAW: "It's a draw"
}

RE_DICT = {
    GameState.PLACE: '([a-f])\s*([1-6])|(quit)',
    GameState.ROTATE: '([1-4])\s*(cw|cc)|(quit)',
    GameState.OVER: '(y|n|)'
}

# Variables
place_pos = (0, 0)

def read_input():
    inp = input(CMD)
    return inp.strip().lower()


def parse_input(inp, state):
    res = re.findall(RE_DICT[state], inp)
    if res:
        if type(res[0]) is tuple:
            return res[0]
        else:
            return tuple(res[0])
    else:
        return tuple()


def compute_input(game, state, inp):
    # Check syntax
    parsed_inp = parse_input(inp, state)
    while not state == GameState.OVER and not parsed_inp:
        print(INPUT_ERROR)
        parsed_inp = parse_input(read_input(), state)

    # Quit if requested
    if QUIT_CMD in parsed_inp:
        return GameState.QUIT

    if state == GameState.PLACE:
        global place_pos

        place_pos = [ROW_IDS.index(parsed_inp[1]), COL_IDS.index(parsed_inp[0])]
        return GameState.ROTATE

    elif state == GameState.ROTATE:
        index = int(parsed_inp[0]) - 1
        sections_line = pentago.MATRIX_SIZE / pentago.SECTION_SIZE
        rotate_pos = [int(index / sections_line), int(index % sections_line)]

        verse = ROT_DICT[parsed_inp[1]]
        print(place_pos, rotate_pos, verse)
        succ = game.do_turn(place_pos, rotate_pos, verse)

        return GameState.PLACE

    elif state == GameState.OVER:
        if parsed_inp:
            if parsed_inp[0] == YES:
                game.restart()
                return GameState.PLACE
            elif parsed_inp[0] == NO or parsed_inp[0] == '':
                return GameState.QUIT
        else:
            return GameState.QUIT


def clear():
    if sysname == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def hor_line():
    output = 2 * SPACE
    for i in range(2 + 2 + pentago.MATRIX_SIZE * 2 + 1):
        output += HOR_SEP
    output += '\n'
    return output


def section_hor_line():
    output = VERT_SEP
    for i in range(1 + 2 + pentago.MATRIX_SIZE * 2):
        output += HOR_SEP
    output += VERT_SEP + '\n'
    return output


def print_turn(game):
    print(TURN_STRING + WINNER_DICT[game.cur_turn] + '\n')


def print_matrix(matrix):
    output = ''

    # Column names
    output += 4 * SPACE + SPACE.join(COL_IDS[:3]) + 3 * SPACE \
              + SPACE.join(COL_IDS[3:6]) + '\n'
    output += hor_line()

    for i in range(pentago.MATRIX_SIZE):
        # Row names
        output += ROW_IDS[i] + SPACE
        output += VERT_SEP + SPACE

        for j in range(len(matrix[i])):
            cell = matrix[i][j]

            output += (colored(PAWN, COLORS[cell])
                       if cell != pentago.BLANK else ' ') + ' '

            if (j + 1) % pentago.SECTION_SIZE == 0 and j + 1 != pentago.MATRIX_SIZE:
                output += VERT_SEP + SPACE

        output += VERT_SEP + '\n'

        if (i + 1) % pentago.SECTION_SIZE == 0 and i + 1 != pentago.MATRIX_SIZE:
            #output += section_hor_line()
            output += SPACE * 2 + MIDDLE_LINE + '\n' # Hardcoded Way

        i += 1

    output += hor_line()
    print(output)


def print_status(state, gamestatus):
    str = '' if gamestatus == pentago.DRAW else STATUS_DICT[state]

    if state == GameState.OVER:
        str = str.replace(WINNER_TOKEN, WINNER_DICT[gamestatus])
    print(str)


def main():
    # Init
    clear()
    inp = ''

    # Pentago model
    game = turn_controller.TurnController()

    """
    for i in range(4):
        for j in range(2):
            game.do_turn((i, j), (1, 1), pentago.CLOCKWISE)
    """

    state = GameState.PLACE

    # Pentago title
    pentago_text = open(path.join(path.dirname(__file__), TITLE_FILENAME)).read()

    # Game loop
    while state != GameState.QUIT:

        print(pentago_text)

        # Check if someone won
        gamestatus = game.game.status()
        if gamestatus != pentago.BLANK:    # Someone is winning
            state = GameState.OVER

        print_turn(game)
        print_matrix(game.game_matrix)
        print_status(state, gamestatus)

        inp = read_input()
        state = compute_input(game, state, inp)

        clear()


if __name__ == '__main__':
    main()
