import model.turn_controller as turn_controller
import model.pentago as pentago

from os import system, path, name as sysname
from termcolor import colored

TITLE_FILENAME = 'files/title.txt'

CMD = '>> '
QUIT_CMD = 'quit'
NEW_GAME = 'new_game'

hor_test = '─/┼/╬/═/║'

PAWN = 'O'
VERT_SEP = '║'
HOR_SEP = '═'
SPACE = ' '


COLORS = { pentago.WHITE: 'white', pentago.BLACK: 'red' }


def read_input():
    inp = input(CMD)
    return inp.strip().lower()


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
            output += '║═══════╬═══════║\n' # Hardcoded Way

        i += 1

    output += hor_line()
    print(output)

def main():
    # Init
    clear()
    inp = ''

    # Pentago model
    game = turn_controller.TurnController()
    for i in range(6):
        for j in range(6):
            game.do_turn((i, j), (0, 0), pentago.CLOCKWISE)

    # Pentago title
    pentago_text = open(path.join(path.dirname(__file__), TITLE_FILENAME)).read()

    # Game loop
    while inp != QUIT_CMD:

        print(pentago_text)

        print_matrix(game.game_matrix)
        inp = read_input()
        clear()

if __name__ == '__main__':
    main()
