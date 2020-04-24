import model.pentago as pentago


class TurnController:
    def __init__(self, first=pentago.BLACK):
        """ Construct3 a new pentago game.

        `first` is pentago.BLACK or pentago.WHITE, represents which color will
        start the match.
        """
        self._turns = [pentago.BLACK, pentago.WHITE]
        self._cur_turn = first
        self._game = pentago.Pentago()

    def do_turn(self, place_point, rotate_section, rotate_verse):
        """ Execute one game turn.

        `point` is in the form (row, colum). The pawn color is defined by
        the current turn
        `rotate_section` is in the form (row, column)
        `rotate_verse` is CLOCKWISE or COUNTCLOCKWISE
        Return True if the turn was successful(the pawn could be placed), False
        else.
        """
        # Place a pawn
        succ = self._game.place(self._cur_turn, place_point)

        # Check if it's already won
        status = self._game.status()
        if status in self._turns:
            return status

        # Rotate
        if succ:
            self._game.rotate(rotate_section, rotate_verse)

            # Next turn
            self._cur_turn = self._turns[self._turns.index(self._cur_turn) - 1]

        return succ

    def restart(self):
        """Starts a new pentago game, deleting all the progress."""
        self._game = pentago.Pentago()

    @property
    def cur_turn(self):
        return self._cur_turn

    @property
    def game_matrix(self):
        return self._game.matrix

    @property
    def game(self):
        return self._game
