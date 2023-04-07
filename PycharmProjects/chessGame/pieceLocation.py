
def piece_location():
    pass

class pieces():
    def __init__(self):
        pass





def setup_chessboard():
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

chessboard=setup_chessboard()

piece_location_array=[[0 for x in range(8)] for y in range(8)]
piece_location_array=dict()
for i in range (len(chessboard)):
    for j in range (len(chessboard[i])):
        piece = chessboard[i][j]
        if piece==' X ':
            pass
        else:
            piece_location_array[i]={(i,j):piece}

print(piece_location_array.keys())
print(piece_location_array)









