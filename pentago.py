import copy


BLANK = 0
WHITE = 1
BLACK = 2
CLOCKWISE = True
COUNTCLOCKWISE = False

SECTION_SIZE = 3

class Pentago:
    """ Model class for the game state. """

    def __init__(self):
        """ Contruct a new pentago game model. """
        self.matrix = []
        for i in range(6):
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
