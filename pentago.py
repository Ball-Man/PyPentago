import copy


BLANK = 0
WHITE = 1
BLACK = 2
CLOCKWISE = True
COUNTCLOCKWISE = False

SECTION_SIZE = 3

class Pentago:
    def __init__(self):
        self.matrix = []
        for i in range(6):
            self.matrix.append([BLANK, BLANK, BLANK, BLANK, BLANK, BLANK])

    def place(self, color, point):
        if self.matrix[point[0]][point[1]] != BLANK:
            return False

        self.matrix[point[0]][point[1]] = color
        return True

    def rotate(self, section, verse):
        result = copy.deepcopy(self.matrix)
        for i in range(section[0] * SECTION_SIZE, section[0] * SECTION_SIZE + SECTION_SIZE):
            for j in range(section[1] * SECTION_SIZE, section[1] * SECTION_SIZE + SECTION_SIZE):
                result[i][j] = self.matrix[SECTION_SIZE - 1 - j][i]

        self.matrix = result
