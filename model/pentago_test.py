import model.pentago as pentago

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

    for i in range(1, 6):
        for j in range(6):
            game.place(pentago.BLACK, (i, j))
    # Assert on content
    assert(game.full())
    # Assert on game status(draw on doublewin)
    assert(game.status() == pentago.DRAW)

    game = pentago.Pentago()
    # Assert on game not over
    assert(game.status() == pentago.BLANK)

    for i in range(6):
        game.place(pentago.WHITE, (i, 0))
    # Assert on vertical winning
    assert(game.status() == pentago.WHITE)
    for i in range(1, 6):
        for j in range(6):
            game.place(pentago.BLACK, (j, i))
    # Assert on game status(draw on doublewin)
    assert(game.status() == pentago.DRAW)

    game = pentago.Pentago()
    for j in range(5):
        game.place(pentago.BLACK, (j, j))
    assert(game.status() == pentago.BLACK)

    game = pentago.Pentago()
    for j in range(5):
        game.place(pentago.BLACK, (j, pentago.MATRIX_SIZE - 1 - j))
    assert(game.status() == pentago.BLACK)

if __name__ == '__main__':
    test()
