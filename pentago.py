import copy


BLANK = 0
WHITE = 1
BLACK = 2
CLOCKWISE = True
COUNTCLOCKWISE = False

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
        for i in range(len(self.matrix) // 2):
            for j in range(len(self.matrix[i]) // 2):
                result[i][j] = self.matrix[len(self.matrix[i]) // 2 - 1 - j][i]

        self.matrix = result
