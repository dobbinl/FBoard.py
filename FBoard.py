# Author: Lori Dobbin
# Date: March 12, 2020
# Description: A board(grid) game where player x is trying to get to a square; and player o is trying block x.

class FBoard():
    # create 8x8 board
    def __init__(self):
        self._board = [
            ['x', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', 'o'],
            ['', '', '', '', '', '', 'o', ''],
            ['', '', '', '', '', 'o', '', 'o']
        ]

        self._state = 'UNFINISHED'  # 'X_WON' 'O_WON' 'UNFINISHED'
        self._x_position = [0, 0]

    def displayBoard(self):
        print()
        for row in range(8):
            s = ''
            for col in range(8):
                if self._board[row][col] != '':
                    s += self._board[row][col]
                else:
                    s += '-'
            print(s)

    def get_game_board(self):
        return self._board

    def get_game_state(self):
        return self._state

    def move_x(self, row, column):
        if self._state != 'UNFINISHED':
            return False

        current_row, current_column = self._x_position

        if not self.check_x_allowed(row, column):
            return False

        self._board[row][column] = 'x'
        self._board[current_row][current_column] = ''
        self._x_position = [row, column]

        if (row == 7 and column == 7):
            self._state = 'X_WON'

        return True

    def move_o(self, start_row, start_column, end_row, end_column):
        if self._state != 'UNFINISHED':
            return False

        if (self._board[start_row][start_column] != 'o'):
            return False

        if (not self.check_y_allowed(end_row, end_column, start_row, start_column)):
            return False
        #current_row, current_column = self._o_position
        self._board[end_row][end_column] = 'o'
        self._board[start_row][start_row] = ''

        # is there any valid move for x
        current_x_row, current_x_column = self._x_position
        possible_locations_for_x = (
            (current_x_row - 1, current_x_column - 1),
            (current_x_row - 1, current_x_column + 1),
            (current_x_row + 1, current_x_column - 1),
            (current_x_row + 1, current_x_column + 1)
        )
        is_all_new_locations_invalid = False
        c = 0
        for new_loc in possible_locations_for_x:

            if (new_loc[0] < 0 or new_loc[0] > 7 or new_loc[1] < 0 or new_loc[1] > 7 or
                    self._board[new_loc[0]][new_loc[1]] == 'o'):
                c += 1

        if c == 4:
            is_all_new_locations_invalid = True

            # is_all_new_locations_invalid and (new_loc[0] < 0 or new_loc[0] > 7 or new_loc[1] < 0 or new_loc[1] > 7 or
            # self._board[new_loc[0]][new_loc[1]] == 'o')
        if (is_all_new_locations_invalid):
            self._state = 'O_WON'
        return True

    def check_x_allowed(self, new_row, new_column):
        cur_row, cur_col = self._x_position
        if (0 <= new_row and \
                new_row <= 7 and \
                0 <= new_column and \
                new_column <= 7 and \
                self._board[new_row][new_column] != 'o' and \
                new_row - cur_row in (-1, 1) and new_column - cur_col in (-1, 1)):
            return True
        # if ( ((new_row - cur_row) in (-1, 1) and (new_column - cur_col) in (-1, 1))):
        # return True
        return False


    def check_y_allowed(self, new_row, new_column, cur_row, cur_col):
        if (0 <= new_row and \
                new_row <= 7 and \
                0 <= new_column and \
                new_column <= 7 and \
                self._board[new_row][new_column] != 'o' and \
                self._board[new_row][new_column] != 'x' and \
                new_row - cur_row in (-1, 1) and new_column - cur_col in (-1, 1) and \
                (new_row - cur_row, new_column - cur_col) != (1 ,1)):
            return True
        return False

fb = FBoard()
while fb.get_game_state() == 'UNFINISHED':
    fb.displayBoard()
    # run an x turn
    xrow, xcol = -1, -1
    while not fb.move_x(xrow, xcol):
        xrow = int(input('Enter new row for x piece: '))
        xcol = int(input('Enter new column for x piece: '))
        # fb.move_x(xrow, xcol)
    # run an o turn
    fb.displayBoard()
    orowS, ocolS, orowE, ocolE = -1 ,-1 ,-1 ,-1
    while not fb.move_o(orowS, ocolS, orowE, ocolE):
        orowS = int(input('Enter start row for o piece: '))
        ocolS = int(input('Enter start column for 0 piece: '))
        orowE = int(input('Enter new row for o piece: '))
        ocolE = int(input('Enter new column for o piece: '))


# fb.move_x(2, 0)
# fb.displayBoard()
# fb.move_o(6, 6, 5, 5)
# fb.displayBoard()
# print()
# print(fb.get_game_state())