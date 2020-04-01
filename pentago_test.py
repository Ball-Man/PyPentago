import pentago

def print_matrix(matrix):
    for lst in matrix:
        print(lst)
    print()

def test():
    game = pentago.Pentago()

    game.place(pentago.WHITE, (0, 0))
    game.place(pentago.WHITE, (3, 3))
    #print_matrix(game.matrix)

    game.rotate((0, 0), pentago.CLOCKWISE)
    game.rotate((1, 1), pentago.CLOCKWISE)
    #print_matrix(game.matrix)

    game.rotate((0, 0), pentago.COUNTCLOCKWISE)
    game.rotate((1, 1), pentago.COUNTCLOCKWISE)
    #print_matrix(game.matrix)

    # Assert on rotation
    assert(game.place(pentago.WHITE, (0, 0)) == False)

    for i in range(6):
        game.place(pentago.WHITE, (0, i))
    # Assert on horizontal winning
    assert(game.status() == pentago.WHITE)

if __name__ == '__main__':
    test()
