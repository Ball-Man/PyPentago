import pentago

def print_matrix(matrix):
    for lst in matrix:
        print(lst)
    print()

def test():
    game = pentago.Pentago()

    game.place(pentago.WHITE, (0, 0))
    print_matrix(game.matrix)

    game.rotate((0, 0), pentago.CLOCKWISE)
    print_matrix(game.matrix)

if __name__ == '__main__':
    test()
