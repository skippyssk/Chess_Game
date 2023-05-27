"""
import possibleMoves

RookMovesDown = possibleMoves.RookDownLegal()
RookMovesUp = possibleMoves.RookUpLegal()
RookMovesRight = possibleMoves.RookRightLegal()
RookMovesLeft = possibleMoves.RookLeftLegal()
i = 0
j = 0
RookMovesD = [[0 for x in range(2)] for y in range(4)]
while i < len(RookMovesDown) / 2:
    Storage = []
    Storage.append(RookMovesDown[j])
    Storage.append(RookMovesDown[j + 1])
    RookMovesD[i][0] = Storage[0]
    RookMovesD[i][1] = Storage[1]
    i += 1;
    j += 2

RookMovesU = [[0 for x in range(2)] for y in range(4)]
while i < len(RookMovesUp) / 2:
    Storage = []
    Storage.append(RookMovesUp[j])
    Storage.append(RookMovesUp[j + 1])
    RookMovesU[i][0] = Storage[0]
    RookMovesU[i][1] = Storage[1]
    i += 1;
    j += 2
BR1Moves = [[0 for x in range(2)] for y in range(2)]
BR1Moves[0] = RookMovesDown
BR1Moves[1] = RookMovesUp

print(BR1Moves)

UpdateBR1Moves = [[0 for x in range(2)] for y in range(4)]
i = 0;
j = 0
while j < len(BR1Moves[j]) / 2:
    i = 0;
    j = 0
    while i < len(BR1Moves[0]) / 2:
        Storage = []
        Storage.append(BR1Moves[j])
        Storage.append(BR1Moves[j + 1])
        UpdateBR1Moves[i][j] = Storage[0]
        UpdateBR1Moves[i][j + 1] = Storage[1]
        i += 1
    j += 1

print(UpdateBR1Moves)

import mainChess
import Piece_location
import numpy as np
firstMove=True

def Piece_position_array():
    Piece_array= np.array([[mainChess.BR1_pos], [mainChess.BN1_pos], [mainChess.Bb1_pos], [mainChess.BK_pos],
                    [mainChess.BQ_pos], [mainChess.Bb2_pos],[mainChess.BN2_pos], [mainChess.BR2_pos],
                    [mainChess.BP1_pos], [mainChess.BP2_pos], [mainChess.BP3_pos], [mainChess.BP4_pos],
                    [mainChess.BP5_pos], [mainChess.BP6_pos], [mainChess.BP7_pos], [mainChess.BP8_pos],
                    [mainChess.WR1_pos], [mainChess.WN1_pos], [mainChess.Wb1_pos], [mainChess.WK_pos],
                    [mainChess.WQ_pos], [mainChess.Wb2_pos],[mainChess.WN2_pos], [mainChess.WR2_pos],
                    [mainChess.WP1_pos],[mainChess.WP2_pos], [mainChess.WP3_pos], [mainChess.WP4_pos],
                    [mainChess.WP5_pos], [mainChess.WP6_pos], [mainChess.WP7_pos], [mainChess.WP8_pos]])

    return Piece_array

compare_pieces=Piece_position_array()

def compare_arrays(arr1, compare_pieces):
    return np.any(np.all(arr1 == compare_pieces, axis = 2))

def PosObsDown():

    i=mainChess.BR1_pos[0]+1
    j=mainChess.BR1_pos[1]

    while i <= 7:


        compare = [i,j]


        if compare_arrays(compare, compare_pieces):
            print("yes")
            print(compare)
            return compare
        else:
            i += 1

    return 0

def RookMoveDownBeforeObs(PositionOfObstacleDown):

    i=mainChess.BR1_pos[0]+1
    j=mainChess.BR1_pos[1]
    iMove=PositionOfObstacleDown[0]
    jMove=PositionOfObstacleDown[1]

    iMovable=iMove-i
    jMovable=jMove-j
    RookMoveArray=[]
    while i<iMove:
        RookMoveArray+=[i,j]
        i+=1
    RookMoveArray+=[i,j]
    return RookMoveArray



def RookDownLegal():

    PositionOfObstacleDown=PosObsDown()

    RookRowArrayDown = []
    RookMoveArray_listDown = RookMoveDownBeforeObs(PositionOfObstacleDown)
    print(RookMoveArray_listDown)
    for i in range(0, len(RookMoveArray_listDown), 2): # start from index 1 and step by 2
        RookRowArrayDown.append(RookMoveArray_listDown[i])


    return RookMoveArray_listDown

def PosObsUp():

    i=mainChess.BR1_pos[0]-1
    j=mainChess.BR1_pos[1]

    while i >= 0:


        compare = [i,j]


        if compare_arrays(compare, compare_pieces):
            print("yes")
            print(compare)
            return compare
        else:
            i -= 1

    return 0

def RookMoveUpBeforeObs(PositionOfObstacleUp):

    i=mainChess.BR1_pos[0]-1
    j=mainChess.BR1_pos[1]
    iMove=PositionOfObstacleUp[0]
    jMove=PositionOfObstacleUp[1]

    iMovable=iMove-i
    jMovable=jMove-j
    RookMoveArray=[]
    while i>iMove:
        RookMoveArray+=[i,j]
        i-=1
    RookMoveArray+=[i,j]
    return RookMoveArray



def RookUpLegal():

    PositionOfObstacleUp=PosObsUp()

    RookRowArrayUp = []
    RookMoveArray_listUp = RookMoveUpBeforeObs(PositionOfObstacleUp)
    print(RookMoveArray_listUp)



    return RookMoveArray_listUp

def PosObsRight():

    i=mainChess.BR1_pos[0]
    j=mainChess.BR1_pos[1]+1

    while j <= 7:


        compare = [i,j]


        if compare_arrays(compare, compare_pieces):
            print("yes")
            print(compare)
            return compare
        else:
            j += 1

    return compare

def RookMoveRightBeforeObs(PositionOfObstacleRight):

    i=mainChess.BR1_pos[0]
    j=mainChess.BR1_pos[1]+1
    iMove=PositionOfObstacleRight[0]
    jMove=PositionOfObstacleRight[1]

    iMovable=iMove-i
    jMovable=jMove-j
    RookMoveArray=[]
    while j<jMove:
        RookMoveArray+=[i,j]
        j+=1
    RookMoveArray+=[i,j]
    return RookMoveArray



def RookRightLegal():

    PositionOfObstacleRight=PosObsRight()

    RookRowArrayRight = []
    RookMoveArray_listRight = RookMoveRightBeforeObs(PositionOfObstacleRight)
    print(RookMoveArray_listRight)
    for i in range(1, len(RookMoveArray_listRight), 2): # start from index 1 and step by 2
        RookRowArrayRight.append(RookMoveArray_listRight[i])


    return RookRowArrayRight


def PosObsLeft():

    i=mainChess.BR1_pos[0]
    j=mainChess.BR1_pos[1]-1

    while j >=0 :


        compare = [i,j]


        if compare_arrays(compare, compare_pieces):
            print("yes")
            print(compare)
            return compare
        else:
            j -= 1

    return compare

def RookMoveLeftBeforeObs(PositionOfObstacleLeft):

    i=mainChess.BR1_pos[0]
    j=mainChess.BR1_pos[1]-1
    iMove=PositionOfObstacleLeft[0]
    jMove=PositionOfObstacleLeft[1]

    iMovable=iMove-i
    jMovable=jMove-j
    RookMoveArray=[]
    while j>jMove:
        RookMoveArray+=[i,j]
        j-=1
    RookMoveArray+=[i,j]
    return RookMoveArray



def RookLeftLegal():

    PositionOfObstacleLeft=PosObsLeft()

    RookRowArrayLeft = []
    RookMoveArray_listLeft = RookMoveLeftBeforeObs(PositionOfObstacleLeft)
    print(RookMoveArray_listLeft)


    return RookMoveArray_listLeft


def PawnObj():
    i=mainChess.BP1_pos[0]+1
    j=mainChess.BP1_pos[1]
    I=mainChess.BP1_pos[0]
    while i<= I:
        compare = [i,j]


        if compare_arrays(compare, compare_pieces):
            print("yes")
            print(compare)
            return compare
        else:
            i += 1

    return 0


print(RookUpLegal())
print(RookDownLegal())
"""