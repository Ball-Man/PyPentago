import turn_controller
import pentago

def test():
    controller = turn_controller.TurnController()
    for i in range(10):
        row = i % 2
        res = controller.do_turn((row, int(i / 2)), (1, 1), pentago.CLOCKWISE)
        if i < 8:
            assert(res == pentago.BLANK)
        elif i >= 8:
            assert(res == pentago.BLACK)

if __name__ == '__main__':
    test()
