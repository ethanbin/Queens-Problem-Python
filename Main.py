import copy
from tkinter import *

# these codes indicate the status of a position in the board
CONST_CODE_EMPTY = 0
CONST_CODE_BLOCKED = -1
CONST_CODE_QUEEN = 1

class Board:
    _solutions = list()
    _solution_index = 0

    def __init__(self, size: int):
        self._size = size
        self._queen_count = 0
        self._board = [[0 for x in range(size)] for y in range(size)]
        return

    def get_size(self):
        return self._size

    def get_queen_count(self):
        return self._queen_count

    def print_board(self):
        formatted_board = ""
        white_cell = True
        for row in self._board:
            for col in row:
                if col == CONST_CODE_QUEEN:
                    formatted_board += "Q "
                else:
                    if white_cell:
                        formatted_board += u"\u25A1 "
                    else:
                        formatted_board += u"\u25A0 "
                white_cell = not white_cell
            white_cell = not white_cell
            formatted_board += "\n"
        return formatted_board

    def print_board_2(self):
        formatted_board = "   "
        for i in range(self.get_size()):
            formatted_board += str(i+1) + "  "
        formatted_board += "\n\n"

        for i in range(self.get_size()):
            formatted_board += str(i+1) + "  "
            for j in range(self.get_size()):
                if self._board[i][j] == CONST_CODE_QUEEN:
                    formatted_board += "Q  "
                else:
                    formatted_board += "-  "
            formatted_board += "\n\n"
        return formatted_board

    def print_board_debug(self):
        for row in self._board:
            for col in row:
                if col == CONST_CODE_QUEEN:
                    print('Q', end=" ")
                elif col == CONST_CODE_BLOCKED:
                    print('X ', end="")
                else:
                    print('_', end=" ")
            print()

    # insert a queen (1) into a board at a given location
    def insert_queen(self, row: int, col: int) -> bool:
        # if location outside of board, return false
        if row < 0 or col < 0 or row >= self._size or col >= self._size:
            return False
        # if queen cannot be placed in given location, return false
        if self._board[row][col] != CONST_CODE_EMPTY:
            return False
        self._board[row][col] = CONST_CODE_QUEEN
        self._queen_count += 1

        # filling blocked positions with CONST_CODE_BLOCKED
        for i in range(self._size):
            # set recentlyInsertedRow of newest queen to be blocked if empty
            if self._board[row][i] == CONST_CODE_EMPTY:
                self._board[row][i] = CONST_CODE_BLOCKED
            # set column of newest queen to be blocked if empty
            if self._board[i][col] == CONST_CODE_EMPTY:
                self._board[i][col] = CONST_CODE_BLOCKED

            # do diagonal from piece to bottom right
            blocked_row = row + i
            blocked_col = col + i
            if blocked_row < self._size and blocked_col < self._size and \
                    self._board[blocked_row][blocked_col] == CONST_CODE_EMPTY:
                self._board[blocked_row][blocked_col] = CONST_CODE_BLOCKED

            # do diagonal from piece to top left
            blocked_row = row - i
            blocked_col = col - i
            if blocked_row >= 0 and blocked_col >= 0 and self._board[blocked_row][blocked_col] == CONST_CODE_EMPTY:
                self._board[blocked_row][blocked_col] = CONST_CODE_BLOCKED

            # do diagonal from piece to top right
            blocked_row = row - i
            blocked_col = col + i
            if blocked_row >= 0 and blocked_col < self._size and \
                    self._board[blocked_row][blocked_col] == CONST_CODE_EMPTY:
                self._board[blocked_row][blocked_col] = CONST_CODE_BLOCKED

            # do diagonal from piece to bottom left
            blocked_row = row + i
            blocked_col = col - i
            if blocked_row < self._size and blocked_col >= 0 and \
                    self._board[blocked_row][blocked_col] == CONST_CODE_EMPTY:
                self._board[blocked_row][blocked_col] = CONST_CODE_BLOCKED
        return True

    @staticmethod
    def add_solution(board) -> bool:
        if board is None or not isinstance(board, Board):
            return False
        if board.get_queen_count() != board.get_size():
            return False
        Board._solutions.append(board)
        return True

    @staticmethod
    def get_current_solution():
        if len(Board._solutions) < 1:
            return None
        if Board._solution_index >= len(Board._solutions) or \
                Board._solution_index < 0:
            return None
        return Board._solutions[Board._solution_index]

    @staticmethod
    def get_current_solution_index() -> int:
        return Board._solution_index

    @staticmethod
    def next_solution():
        if len(Board._solutions) > 0:
            Board._solution_index = (Board._solution_index + 1) % len(Board._solutions)
            return Board.get_current_solution()

    @staticmethod
    def last_solution():
        if len(Board._solutions) > 0:
            Board._solution_index = (Board._solution_index - 1) % len(Board._solutions)
            return Board.get_current_solution()

def depth_first_search(board: Board, current_row: int):
    for i in range(board.get_size()):
        child = copy.deepcopy(board)
        piece_inserted = child.insert_queen(i, current_row)
        # if child has 8 pieces, it is a solution and will have no more children,
        # so add to list of solutions and exit this recursive call
        if child.get_queen_count() >= board.get_size():
            Board.add_solution(child)
            return
        # if child had a piece inserted but is not yet a solution, traverse down this child
        if piece_inserted:
            depth_first_search(child, current_row+1)


class Window(Frame):
    def __init__(self, master=None):
        self._displayed_solution = StringVar()
        self._solution_number = StringVar()
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        self._displayed_solution.set(Board.get_current_solution().print_board_2())
        board_label = Label(self, textvariable=self._displayed_solution, font=("Courier", 16))
        board_label.pack()

        self._solution_number.set(1)
        solution_number_label = Label(self, textvariable=self._solution_number, font=("Courier", 16))
        solution_number_label.pack()
        solution_number_label.place(relx=.5, rely=.95, anchor=CENTER)

        # creating a button instance
        last_button = Button(self, text="Last Solution", command=lambda: self.last_solution())
        next_button = Button(self, text="Next Solution", command=lambda: self.next_solution())

        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)


        # placing the button on my window
        last_button.place(relx=.1, rely=.95, anchor=CENTER)
        next_button.place(relx=.9, rely=.95, anchor=CENTER)

    def last_solution(self):
        self._displayed_solution.set(Board.last_solution().print_board_2())
        self._solution_number.set(Board.get_current_solution_index() + 1)

    def next_solution(self):
        self._displayed_solution.set(Board.next_solution().print_board_2())
        self._solution_number.set(Board.get_current_solution_index() + 1)

    def left_key(self, event):
        self.last_solution()

    def right_key(self, event):
        self.next_solution()


def main():
    size = 8
    starting_board = Board(size)
    depth_first_search(starting_board, 0)

    root = Tk()
    root.resizable(False, False)
    root.geometry("450x450")
    # height = int(root.winfo_screenheight() / 2)
    # root.geometry("{}x{}".format(height, height))
    Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
