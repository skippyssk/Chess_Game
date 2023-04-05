from Piece_location import BR1_position
import LegalChessMoves

def beginning_chessboard_creator():
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


chessboard = beginning_chessboard_creator()


def chessboard_update(
    user_input_row,
    user_input_column,
    user_input_row_going,
    user_input_column_going,
    chessboard,
):
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




import Piece_location 

chessboard = beginning_chessboard_creator()

game_playing = True

while game_playing:
    illegal = True
    while illegal:
        try:
            input_row = int(input("Please enter a number for the row: "))
            illegal = False
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            illegal = True
    illegal = True
    while illegal:
        try:
            input_column = int(input("Please enter a number for the column: "))
            illegal = False
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            illegal = True
    illegal = True
    while illegal:
        try:
            input_row_to = int(input("Please enter a number for the row: "))
            illegal = False
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            illegal = True
    illegal = True
    while illegal:
        try:
            input_column_to = int(input("Please enter a number for the column: "))
            illegal = False
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            illegal = True

     
    chessboard_update(input_row, input_column, input_row_to, input_column_to, chessboard)
    BR1_pos = Piece_location.BR1_position(chessboard)
    BN1_pos = Piece_location.BN1_position(chessboard)
    Bb1_pos = Piece_location.Bb1_position(chessboard)
    BK_pos = Piece_location.BK_position(chessboard)
    BQ_pos = Piece_location.BQ_position(chessboard)
    Bb2_pos = Piece_location.Bb2_position(chessboard)
    BN2_pos = Piece_location.BN2_position(chessboard)
    BR2_pos = Piece_location.BR2_position(chessboard)
    BP1_pos = Piece_location.BP1_position(chessboard)
    BP2_pos = Piece_location.BP2_position(chessboard)
    BP3_pos = Piece_location.BP3_position(chessboard)
    BP4_pos = Piece_location.BP4_position(chessboard)
    BP5_pos = Piece_location.BP5_position(chessboard)
    BP6_pos = Piece_location.BP6_position(chessboard)
    BP7_pos = Piece_location.BP7_position(chessboard)
    BP8_pos = Piece_location.BP8_position(chessboard)
    WR1_pos = Piece_location.WR1_position(chessboard)
    WN1_pos = Piece_location.WN1_position(chessboard)
    Wb1_pos = Piece_location.Wb1_position(chessboard)
    WK_pos = Piece_location.WK_position(chessboard)
    WQ_pos = Piece_location.WQ_position(chessboard)
    Wb2_pos = Piece_location.Wb2_position(chessboard)
    WN2_pos = Piece_location.WN2_position(chessboard)
    WR2_pos = Piece_location.WR2_position(chessboard)
    WP1_pos = Piece_location.WP1_position(chessboard)
    WP2_pos = Piece_location.WP2_position(chessboard)
    WP3_pos = Piece_location.WP3_position(chessboard)
    WP4_pos = Piece_location.WP4_position(chessboard)
    WP5_pos = Piece_location.WP5_position(chessboard)
    WP6_pos = Piece_location.WP6_position(chessboard)
    WP7_pos = Piece_location.WP7_position(chessboard)
    WP8_pos = Piece_location.WP8_position(chessboard)
    
    
    
    game_playing = input("would you like to keep playing?")
    if game_playing.lower() == "no":
        game_playing = False
    else:
        game_playing = True