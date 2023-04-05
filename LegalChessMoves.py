import possibleMoves


RookMovesDown=possibleMoves.RookDownLegal()
RookMovesUp=possibleMoves.RookUpLegal()
RookMovesRight=possibleMoves.RookRightLegal()
RookMovesLeft=possibleMoves.RookLeftLegal()
i=0
j=0
RookMovesD=[[0 for x in range (2)]for y in range(4)]
while i < len(RookMovesDown)/2:
    Storage=[]
    Storage.append(RookMovesDown[j])
    Storage.append(RookMovesDown[j+1])
    RookMovesD[i][0]=Storage[0]
    RookMovesD[i][1]=Storage[1]
    i+=1; j+=2

RookMovesU=[[0 for x in range (2)]for y in range(4)]
while i < len(RookMovesUp)/2:
    Storage=[]
    Storage.append(RookMovesUp[j])
    Storage.append(RookMovesUp[j+1])
    RookMovesU[i][0]=Storage[0]
    RookMovesU[i][1]=Storage[1]
    i+=1; j+=2
BR1Moves=[[0 for x in range (2)]for y in range(2)]
BR1Moves[0]=RookMovesDown
BR1Moves[1]=RookMovesUp

print(BR1Moves)

UpdateBR1Moves=[[0 for x in range (2)]for y in range(4)]
i=0;j=0
while j < len(BR1Moves[j])/2:
    i=0;j=0
    while i < len(BR1Moves[0])/2:
        Storage=[]
        Storage.append(BR1Moves[j])
        Storage.append(BR1Moves[j+1])
        UpdateBR1Moves[i][j]=Storage[0]
        UpdateBR1Moves[i][j+1]=Storage[1]
        i+=1
    j+=1
    

print(UpdateBR1Moves)
