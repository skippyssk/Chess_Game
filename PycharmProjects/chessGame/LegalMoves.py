import pieceLocation

piece_location_array=pieceLocation.piece_location_array(pieceLocation.piece_location())

print(piece_location_array)
def legal_chess_moves(piece_location_array):
    for i in range(len(piece_location_array)):
        for j in range(len(piece_location_array[i])):
            print(piece_location_array[i][j])

legal_chess_moves(piece_location_array)




"""
we need to scan through the piece location array and find the legal moves
This means that we need to have a way to select different legal moves based
on which one is selected
"""