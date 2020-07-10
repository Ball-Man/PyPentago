from context import *
from pypentago import turn_controller
from pypentago import pentago
from helpers import print_matrix


def test():
    controller = turn_controller.TurnController()
    for i in range(10):
        row = i % 2

        # Assert on current turn
        print(i % 2)
        if (controller.game.status() == pentago.BLANK):
            assert controller.cur_turn == (pentago.BLACK if i % 2 == 0 else
                                           pentago.WHITE)

        res = controller.do_turn((row, int(i / 2)), (1, 1), pentago.CLOCKWISE)
        # Assert on winning condition
        if i < 8:
            assert res
        elif i >= 8:
            assert res
            assert controller.game.status() == pentago.BLACK


if __name__ == '__main__':
    test()
