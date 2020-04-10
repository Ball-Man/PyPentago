import model.turn_controller as turn_controller
import model.pentago as pentago
import enum

from os import system, path, name as sysname
from termcolor import colored

# Constants
TITLE_FILENAME = 'files/title.txt'

CMD = '>> '
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

STATUS_DICT = {
        GameState.PLACE: 'Where do you want to place your pawn? (e.g. b5)',
        GameState.ROTATE: 'What sector do you want to rotate? (e.g. 2cw)'
       }

# Variables
place_pos = (0, 0)

def read_input():
    inp = input(CMD)
    return inp.strip().lower()


def compute_input(game, state, inp):
    # Quit if requested
    if inp == 'quit':
        return GameState.QUIT

    if state == GameState.PLACE:
        # TODO check syntax
        global place_pos

        place_pos = [ROW_IDS.index(inp[1]), COL_IDS.index(inp[0])]
        return GameState.ROTATE

    elif state == GameState.ROTATE:
        # TODO check syntax
        index = int(inp[0]) - 1
        sections_line = pentago.MATRIX_SIZE / pentago.SECTION_SIZE
        rotate_pos = [int(index / sections_line), int(index % sections_line)]

        verse = ROT_DICT[inp[1:]]
        print(place_pos, rotate_pos, verse)
        game.do_turn(place_pos, rotate_pos, verse)

        return GameState.PLACE


def clear():
    if sysname == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def hor_line():
    output = ''
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

def print_matrix(matrix):
    output = ''

    output += hor_line()

    for i in range(pentago.MATRIX_SIZE):
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
            output += MIDDLE_LINE + '\n' # Hardcoded Way

        i += 1

    output += hor_line()
    print(output)

def print_status(state):
    print(STATUS_DICT[state])


def main():
    # Init
    clear()
    inp = ''

    # Pentago model
    game = turn_controller.TurnController()
    """
    for i in range(6):
        for j in range(6):
            game.do_turn((i, j), (0, 0), pentago.CLOCKWISE)
    """
    state = GameState.PLACE

    # Pentago title
    pentago_text = open(path.join(path.dirname(__file__), TITLE_FILENAME)).read()

    # Game loop
    while state != GameState.QUIT:

        print(pentago_text)

        print_matrix(game.game_matrix)
        print_status(state)

        inp = read_input()
        state = compute_input(game, state, inp)
        clear()


if __name__ == '__main__':
    main()
