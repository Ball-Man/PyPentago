import model.turn_controller as turn_controller
import model.pentago as pentago

def test():
    controller = turn_controller.TurnController()
    for i in range(10):
        row = i % 2

        # Assert on current turn
        assert(pentago.BLACK if i % 2 == 0 else pentago.WHITE)

        res = controller.do_turn((row, int(i / 2)), (1, 1), pentago.CLOCKWISE)
        # Assert on winning condition
        if i < 8:
            assert(res == pentago.BLANK)
        elif i >= 8:
            assert(res == pentago.BLACK)


if __name__ == '__main__':
    test()
