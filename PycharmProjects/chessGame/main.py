import chessLogic

class play():
    def __init__(self):
        pass
class pieces():
    def __init__(self):
        pass

    def piece_location(self):
        pass

    def legal_moves(self):
        pass
class chessboard(pieces, play):
    def __init__(self):
        pass

    def setup_chessboard(self):
        x = " X "
        BK = " BK"
        BQ = " BQ"
        WK = " WK"
        WQ = " WQ"

        chessboard = [
            ["BR1", "BN1", "Bb1", BK, BQ, "Bb2", "BN2", "BR2"],
            ["BP1", "BP2", "BP3", "BP4", "BP5", "BP6", "BP7", "BP8"],
            [x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x],
            [x, x, x, x, x, x, x, x],
            ["WP1", "WP2", "WP3", "WP4", "WP5", "WP6", "WP7", "WP8"],
            ["WR1", "WN1", "Wb1", WK, WQ, "Wb2", "WN2", "WR2"],
        ]

        return chessboard



    def update_chessboard(self,user_input_row,
        user_input_column,
        user_input_row_going,
        user_input_column_going,
        chessboard):
        if chessboard[user_input_row_going][user_input_column_going] == " X ":
            (
                chessboard[user_input_row][user_input_column],
                chessboard[user_input_row_going][user_input_column_going]
            ) = (
                chessboard[user_input_row_going][user_input_column_going],
                chessboard[user_input_row][user_input_column]
            )
        else:
            chessboard[user_input_row_going][user_input_column_going] = chessboard[
                user_input_row
            ][user_input_column]
            chessboard[user_input_row][user_input_column] = " X "
        i = 0
        j = 0
        print("\n")
        while j <= 7:
            while i <= 7:
                import sys

                sys.stdout.write(chessboard[j][i] + " ")
                i += 1
            j += 1
            i = 0
            print("\n")
        return chessboard

    def move_choice(self,chessboard):
        move_choice = [0, 0, 0, 0]
        j = 0
        while j <= 3:
            illegal = True
            while illegal:
                try:
                    choice_string = input("please enter a number: ")
                    choice_int = int(choice_string)
                    move_choice[j] = choice_int
                    illegal = False
                except ValueError:
                    if choice_string.lower() == "stop()":
                        print("terminating ....")
                        exit()
                    print("Oops! That was not a valid number. Try again...")
                    illegal = True

            j += 1

        user_input_row = move_choice[0]
        user_input_column = move_choice[1]
        user_input_row_going = move_choice[2]
        user_input_column_going = move_choice[3]

        updated_board=self.update_chessboard(user_input_row, user_input_column, user_input_row_going,
                          user_input_column_going, chessboard)

def play():
    playing=True
    board = chessboard()
    new_board = board.setup_chessboard()
    while playing:

        board.move_choice(new_board)


play()