import copy


BLANK = 0
WHITE = 1
BLACK = 2
DRAW = 3
CLOCKWISE = True
COUNTCLOCKWISE = False

MATRIX_SIZE = 6
SECTION_SIZE = 3

class Pentago:
    """ Model class for the game state. """

    def __init__(self):
        """ Contruct a new pentago game model. """
        self.matrix = []
        self.placed_pawns = 0
        for i in range(MATRIX_SIZE):
            self.matrix.append([BLANK, BLANK, BLANK, BLANK, BLANK, BLANK])

    def place(self, color, point):
        """ Place a pawn on a given point.

        `point` is in the form (row, colum)
        `color` is BLACK or WHITE
        Return True if success, False else
        """
        if self.matrix[point[0]][point[1]] != BLANK:
            return False

        self.matrix[point[0]][point[1]] = color
        self.placed_pawns += 1
        return True

    def rotate(self, section, verse):
        """Rotate one section of the board.

        `section` is in the form (row, column)
        `verse` is CLOCKWISE or COUNTCLOCKWISE
        """
        result = copy.deepcopy(self.matrix)
        for i in range(section[0] * SECTION_SIZE, section[0] * SECTION_SIZE + SECTION_SIZE):
            for j in range(section[1] * SECTION_SIZE, section[1] * SECTION_SIZE + SECTION_SIZE):
                if verse == CLOCKWISE:
                    result[i][j] = self.matrix[SECTION_SIZE - 1 - j][i]
                elif verse == COUNTCLOCKWISE:
                    result[i][j] = self.matrix[j][SECTION_SIZE - 1 - i]

        self.matrix = result

    def full(self):
        """ Check if the matrix is full(True of False). """
        if self.placed_pawns == MATRIX_SIZE ** 2:
            return True
        return False

    def status(self):
        """ Return the current game status

        return BLACK if the black player won,
               WHITE if the white player won,
               DRAW if the game is over but noone won,
               BLANK if the game isn't over(no one won yet).
        """
        winning = []

        # Check rows
        seq_color = BLANK
        counter = 0
        for row in self.matrix:
            for cell in row:
                if cell != seq_color:
                    counter = 0

                if cell == BLANK:
                    counter = 0
                    seq_color = BLANK
                elif cell == WHITE or cell == BLACK:
                    seq_color = cell
                    counter += 1

                if counter == 5:
                    winning.append(seq_color)

        # Check columns
        seq_color = BLANK
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):
                cell = self.matrix[j][i]

                if cell != seq_color:
                    counter = 0

                if cell == BLANK:
                    counter = 0
                    seq_color = BLANK
                elif cell == WHITE or cell == BLACK:
                    seq_color = cell
                    counter += 1

                if counter == 5:
                    winning.append(seq_color)

        # Check Diagonals
        LEFT_DIAG = 0
        RIGHT_DIAG = 1
        DIAG_LEN = 2
        # Metadata matrix, used calculate diagonals in the game
        diag_mat = [[[1, 1] for x in range(MATRIX_SIZE)] for x in range(MATRIX_SIZE)]
        for i in range(MATRIX_SIZE):
            for j in range(MATRIX_SIZE):
                cell = self.matrix[i][j]

                # Update left diagonal metadata
                if i != 0 and j != 0 and cell != BLANK and self.matrix[i - 1][j - 1] == cell:
                    diag_mat[i][j][LEFT_DIAG] += diag_mat[i - 1][j - 1][LEFT_DIAG]

                # Update right diangonal metadata
                if i != MATRIX_SIZE - 1 and j != MATRIX_SIZE - 1 and cell != BLANK and self.matrix[i - 1][j + 1] == cell:
                    diag_mat[i][j][RIGHT_DIAG] += diag_mat[i - 1][j + 1][RIGHT_DIAG]

                # Check if someone won
                for k in range(DIAG_LEN):
                    if diag_mat[i][j][k] == 5:
                        winning.append(cell)

        # Check if for doublewin (draw)
        cur_color = BLANK
        for x in winning:
            if x != cur_color and cur_color != BLANK:
                return DRAW
            cur_color = x

        # Check for winner
        if cur_color != BLANK:
            return cur_color
        elif winning == [] and self.full():
            return DRAW
        elif winning == []:
            return BLANK
